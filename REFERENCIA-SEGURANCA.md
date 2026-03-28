# TOLEDO DIGITAL — REFERÊNCIA DE SEGURANÇA
> Guia técnico para todos os projetos
> Baseado em OWASP Top 10 + boas práticas Spring Boot
> Criado: 28 de Março de 2026

---

## OWASP TOP 10 — O QUE É E COMO APLICAMOS

O OWASP (Open Worldwide Application Security Project) publica anualmente as 10 vulnerabilidades mais críticas em software. Abaixo está o que cada uma significa e como a Toledo Digital a mitiga em todos os projetos.

---

### 1. BROKEN ACCESS CONTROL (Controlo de acesso quebrado)
**O risco:** Utilizadores acedem a recursos que não deveriam (ex: ver pedidos de outro cliente, aceder ao painel admin sem permissão).

**Como mitigamos:**
- Spring Security com `authenticated()` em todas as rotas privadas
- JWT verificado em cada pedido
- Admin routes exigem header `X-Admin-Secret` gerado aleatoriamente
- `.anyRequest().authenticated()` como regra final (fail-safe)

---

### 2. CRYPTOGRAPHIC FAILURES (Falhas criptográficas)
**O risco:** Dados sensíveis em texto simples — passwords, tokens, dados bancários expostos.

**Como mitigamos:**
- Passwords com BCrypt (hash irreversível, custo adaptável)
- JWT assinado com HS256 + secret de 48+ bytes aleatórios
- HTTPS obrigatório em produção (nginx + Let's Encrypt)
- Credenciais em variáveis de ambiente, nunca em código

---

### 3. INJECTION (Injeção — SQL, HTML, etc.)
**O risco:** Atacante injeta código malicioso nas queries da base de dados ou no HTML.

**Como mitigamos:**
- Spring Data JPA com queries parametrizadas (proteção automática SQL injection)
- Nunca construir queries com concatenação de strings
- Validação de inputs no backend (não confiar só no frontend)

---

### 4. INSECURE DESIGN (Design inseguro)
**O risco:** Arquitetura que não foi pensada para segurança desde o início.

**Como mitigamos:**
- Security-first: segurança definida antes de escrever código
- Separação de ambientes (dev com .env local, produção com variáveis do servidor)
- Princípio do mínimo privilégio: cada componente só acede ao que precisa

---

### 5. SECURITY MISCONFIGURATION (Má configuração de segurança)
**O risco:** Headers HTTP expostos, erros detalhados em produção, portas abertas desnecessárias.

**Como mitigamos:**
- Spring Security desativa endpoints desnecessários
- `spring.jpa.show-sql=false` em produção (não expõe queries)
- Nginx configurado para esconder versão do servidor
- robots.txt bloqueia caminhos admin e internos

---

### 6. VULNERABLE COMPONENTS (Componentes vulneráveis)
**O risco:** Bibliotecas desatualizadas com falhas conhecidas.

**Como mitigamos:**
- Maven gerencia dependências com versões explícitas
- Spring Boot BOM garante compatibilidade entre componentes
- Revisão de dependências a cada novo projeto
- Alertas automáticos do GitHub (quando repo ativo)

---

### 7. AUTHENTICATION FAILURES (Falhas de autenticação)
**O risco:** Brute force de passwords, tokens sem expiração, sessões não invalidadas.

**Como mitigamos:**
- Rate limiting: máximo 5 tentativas de login por IP em 15 minutos → HTTP 429
- JWT com expiração de 7 dias
- Sessões stateless (sem server-side sessions que possam ser roubadas)
- BCrypt com custo elevado (torna brute force computacionalmente caro)

---

### 8. SOFTWARE AND DATA INTEGRITY (Integridade de dados)
**O risco:** Dados modificados sem validação (ex: preço do produto alterado no frontend antes de pagar).

**Como mitigamos:**
- Preços sempre validados no backend (nunca confiar no preço enviado pelo cliente)
- Checkout calcula total no servidor, não no browser
- Webhook do Mercado Pago verificado com assinatura antes de processar

---

### 9. LOGGING AND MONITORING (Logs e monitorização)
**O risco:** Ataques não detetados por falta de registos.

**Como mitigamos:**
- Spring Boot Actuator para health checks (`/actuator/health`)
- Logs de tentativas de login falhadas
- Watchdog Jarvis: verifica app a cada 10 min e reinicia se necessário
- `spring.jpa.show-sql=false` em produção (logs limpos)

---

### 10. SERVER-SIDE REQUEST FORGERY (SSRF)
**O risco:** Atacante força o servidor a fazer pedidos HTTP internos (ex: aceder à rede interna).

**Como mitigamos:**
- Nenhum endpoint aceita URLs externas fornecidas pelo utilizador
- Integrações externas (MP, Brevo) usam SDKs oficiais, não URLs dinâmicas

---

## CHECKLIST OBRIGATÓRIA — NOVO PROJETO

```
ANTES DE ESCREVER CÓDIGO
[ ] Gerar JWT_SECRET: openssl rand -base64 48
[ ] Gerar ADMIN_SECRET: openssl rand -hex 24
[ ] Criar .env com credenciais reais (nunca no Git)
[ ] Criar .env.example sem valores reais (no Git)
[ ] Adicionar .env ao .gitignore

DURANTE O DESENVOLVIMENTO
[ ] Todas as rotas admin em .authenticated() no SecurityConfig
[ ] .anyRequest().authenticated() como regra final
[ ] Rate limiting no endpoint de login (/api/auth/login)
[ ] Preços validados no backend no checkout
[ ] robots.txt com /api/admin/ e /api/auth/ bloqueados

ANTES DE ENTREGAR
[ ] HTTPS ativo (certificado SSL válido)
[ ] Testar: aceder /api/admin/ sem credenciais → 401 ou 403
[ ] Testar: 6 logins errados seguidos → 429 na 5ª tentativa
[ ] Testar: payload com preço alterado → backend ignora
[ ] spring.jpa.show-sql=false
[ ] Credenciais do cliente em posse do cliente (não só Toledo)
[ ] .env não está no repositório Git
```

---

## SECRETS — COMO GERAR E GERIR

```bash
# JWT Secret (mínimo 48 bytes / 384 bits)
openssl rand -base64 48

# Admin Secret (32 hex chars = 128 bits)
openssl rand -hex 24

# Nunca reutilizar entre projetos
# Fios MJ tem os seus, Mar de Prata terá os seus, etc.
```

**Onde guardar em produção (VPS cliente):**
```bash
# No servidor do cliente, criar /srv/[projeto]/.env
# com permissões restritas:
chmod 600 /srv/projeto/.env
chown www-data:www-data /srv/projeto/.env

# Arrancar a app carregando o .env:
set -a && source /srv/projeto/.env && set +a
java -jar app.jar
```

---

## NGINX — CONFIGURAÇÃO SEGURA BASE

Para cada projeto entregue, o nginx deve incluir:

```nginx
# Esconder versão do servidor
server_tokens off;

# Headers de segurança
add_header X-Frame-Options "SAMEORIGIN";
add_header X-Content-Type-Options "nosniff";
add_header X-XSS-Protection "1; mode=block";
add_header Referrer-Policy "strict-origin-when-cross-origin";
add_header Permissions-Policy "geolocation=(), microphone=(), camera=()";

# HTTPS forçado
if ($scheme != "https") {
    return 301 https://$host$request_uri;
}
```

---

## ESTADO ATUAL DOS PROJETOS

| Projeto | Credenciais seguras | Rate limiting | SecurityConfig | robots.txt | HTTPS |
|---|---|---|---|---|---|
| Fios MJ | ✅ (corrigido 28/03) | ✅ (implementado 28/03) | ✅ (corrigido 28/03) | ✅ (corrigido 28/03) | ✅ |
| Mar de Prata | ⏳ (em construção) | ⏳ | ⏳ | ⏳ | ⏳ |
| Gabinete | ⏳ (em construção) | ⏳ | ⏳ | ⏳ | ⏳ |

> Mar de Prata e Gabinete nascerão já com todas as práticas aplicadas desde o início.

---

*Toledo Digital · Documento de uso interno · Atualizar após cada projeto*
