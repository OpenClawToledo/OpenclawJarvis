# TOLEDO DIGITAL — SEGURANÇA & CONDUTA PROFISSIONAL
> Documento de referência: auditoria técnica + política de trabalho com clientes
> Criado: 28 de Março de 2026 | Por: Jarvis Soares de Toledo

---

## PARTE 1 — AUDITORIA DE SEGURANÇA (estado atual)

### 🔴 CRÍTICO — Ação imediata

#### 1. Credenciais reais no código-fonte (Fios MJ)
**Problema:** O ficheiro `application.properties` contém dados sensíveis reais:
- Token Mercado Pago (acesso real à conta)
- Token OpenClaw gateway
- Números de telemóvel

Se alguém aceder ao repositório Git (ou ao JAR compilado), tem acesso total a estas contas.

**Solução:**
- Mover para variáveis de ambiente no servidor (nunca no código)
- Usar `.env` local + `.gitignore` para proteger
- Revogar e regenerar os tokens atuais no Mercado Pago (por precaução)

---

#### 2. JWT secret fraco
**Problema:** `jwt.secret=fiosmj-secret-key-2026-super-secure-change-in-prod`
É previsível, curto e está em texto simples no código.

**Solução:**
- Gerar uma chave aleatória de 64+ caracteres: `openssl rand -base64 64`
- Guardar como variável de ambiente no servidor

---

### 🟠 ALTO — Corrigir antes de lançar novos clientes

#### 3. Secret de admin demasiado simples
**Problema:** `admin.secret=fiosmj-admin-2026` — hardcoded no código como valor padrão.
Qualquer pessoa que tente `/api/admin/blog` com o header `X-Admin-Secret: fiosmj-admin-2026` tem acesso total ao painel de blog, newsletter e testemunhos.

**Solução:**
- Gerar um secret aleatório forte (mínimo 32 caracteres)
- Nunca usar datas ou nomes previsíveis

---

#### 4. Rotas de admin abertas no Spring Security
**Problema:** As rotas `/api/admin/blog/**`, `/api/newsletter/**` e `/api/social/**` estão na lista de `permitAll()` no Spring Security — ou seja, o framework não bloqueia, só o controlador faz a verificação manual.

É tecnicamente funcional mas é má prática: se alguém encontrar uma falha na verificação do controlador, não há camada de segurança por baixo.

**Solução:** Mover rotas admin para `.authenticated()` com JWT em vez de `permitAll()`.

---

#### 5. robots.txt não protege caminhos de admin
**Problema:** O robots.txt atual faz `Allow: /` para tudo, incluindo caminhos admin. Motores de busca (e scrapers) podem tentar indexar `/api/admin/`.

**Solução:**
```
User-agent: *
Allow: /
Disallow: /api/admin/
Disallow: /api/auth/
Disallow: /api/cart/
Disallow: /api/orders/
Sitemap: https://fiosmj.com/sitemap.xml
```

---

### 🟡 MÉDIO — Boas práticas

#### 6. Sem rate limiting nas rotas de autenticação
Qualquer bot pode tentar milhares de passwords na rota `/api/auth/login` sem ser bloqueado.

**Solução:** Adicionar rate limiting (ex: máximo 5 tentativas por IP em 15 minutos).

#### 7. CSRF desativado
Aceitável para APIs stateless com JWT, mas deve ser documentado como decisão consciente.

#### 8. `.anyRequest().permitAll()` no final
Qualquer rota não mapeada é pública por omissão. Deve ser `.anyRequest().authenticated()`.

---

### ✅ O QUE ESTÁ BEM

- Passwords com BCrypt (hash seguro) ✅
- JWT com expiração (7 dias) ✅
- HTTPS (SSL via nginx) ✅
- Spring Data JPA — protege contra SQL injection por omissão ✅
- Separação frontend/backend ✅

---

## PARTE 2 — CHECKLIST DE ENTREGA (por projeto)

Antes de entregar qualquer projeto a um cliente, verificar:

### Segurança
- [ ] Credenciais em variáveis de ambiente (não no código)
- [ ] JWT secret forte e único por projeto (nunca reutilizar)
- [ ] Admin secret forte (gerado aleatoriamente)
- [ ] robots.txt com caminhos admin bloqueados
- [ ] HTTPS ativo e certificado SSL válido
- [ ] Teste manual: tentar aceder `/api/admin/` sem credenciais → deve dar 401/403
- [ ] Teste manual: tentar login com password errada 10x → deve bloquear

### Estabilidade
- [ ] App responde em menos de 3 segundos no mobile
- [ ] Teste em iOS Safari + Android Chrome
- [ ] Formulários funcionam (contacto, newsletter, pedido)
- [ ] Imagens carregam corretamente
- [ ] Site funciona sem JavaScript desativado (pelo menos carrega)
- [ ] Sitemap.xml acessível e atualizado
- [ ] Favicon configurado

### Funcionalidades contratadas
- [ ] Cada funcionalidade da proposta foi testada manualmente
- [ ] Cliente testou e aprovou antes do pagamento
- [ ] Documentação básica entregue (como entrar no painel, como editar)

### RGPD / Legal
- [ ] Política de privacidade no ar
- [ ] Termos e condições no ar
- [ ] Aviso de cookies (se aplicável)
- [ ] Dados pessoais só recolhidos com consentimento

---

## PARTE 3 — POLÍTICA DE CONDUTA COM CLIENTES

### Antes de fechar

**O que Toledo diz ao cliente:**
- "Só pagas quando estiveres satisfeito — se não ficares, não pagas."
- "Tens acesso total ao site, podes mudar o que quiseres a qualquer momento."
- "O domínio e o servidor ficam no teu nome — não dependes de mim."
- "Se precisares de suporte, são €30/mês sem contrato de permanência."

**O que Toledo NÃO promete:**
- Resultados de vendas ou de SEO num prazo fixo (Google leva semanas)
- Funcionalidades fora do âmbito acordado sem novo orçamento
- Disponibilidade 24/7 fora do suporte contratado

---

### Durante o projeto

**Regras de ouro para Toledo (funcionário de campo):**

1. **Nunca partilhes credenciais por mensagem de texto** — WhatsApp não é seguro para passwords. Usa email ou entrega pessoalmente.

2. **Documenta tudo** — cada decisão tomada com o cliente fica registada (Jarvis trata disso).

3. **Preview antes de lançar** — o cliente vê e aprova antes de ir ao ar. Sem surpresas.

4. **Alterações fora do âmbito = novo orçamento** — se o cliente pede algo novo após fechar, é trabalho extra. Não é falta de educação dizer isso.

5. **Nunca tens acesso à conta bancária nem ao email principal do cliente** — só ao VPS e ao painel admin do site.

6. **Quando o projeto termina, sai limpo** — entrega todas as credenciais, revoga os teus acessos SSH temporários se não houver suporte contratado.

---

### Após a entrega

| Situação | O que fazer |
|---|---|
| Bug reportado (< 30 dias) | Corrigir sem custo — é garantia |
| Bug reportado (> 30 dias) | Avaliar: se é falha nossa, corrigir; se é novo pedido, orçamentar |
| Cliente pede funcionalidade nova | Novo orçamento, por escrito |
| Cliente fica sem acesso ao painel | Suporte via WhatsApp em dias úteis (se tem suporte contratado) |
| Cliente quer cancelar suporte | Sem problema — dados e acessos continuam dele |
| Cliente quer mudar de fornecedor | Entrega total da documentação e credenciais — sem retenção |

---

## PARTE 4 — PARA PROJETOS FUTUROS (Mar de Prata, Gabinete, etc.)

Cada novo projeto deve nascer já com:

- [ ] Ficheiro `.env` separado por ambiente (dev / produção)
- [ ] JWT secret gerado aleatoriamente (nunca reutilizar entre projetos)
- [ ] Admin secret gerado aleatoriamente
- [ ] Credenciais do cliente em posse do cliente (não só da Toledo Digital)
- [ ] robots.txt com admin bloqueado desde o início
- [ ] HTTPS ativo antes do primeiro deploy público
- [ ] Checklist de entrega preenchida antes de cobrar

---

## RESUMO — O QUE FAZER AGORA (Fios MJ)

| Prioridade | Ação | Quem |
|---|---|---|
| 🔴 | Mover tokens MP e OpenClaw para variáveis de ambiente | Jarvis |
| 🔴 | Regenerar JWT secret (forte, aleatório) | Jarvis |
| 🔴 | Gerar novo admin secret | Jarvis |
| 🟠 | Atualizar robots.txt (bloquear /api/admin/) | Jarvis |
| 🟠 | Corrigir SecurityConfig (admin → authenticated) | Jarvis |
| 🟡 | Adicionar rate limiting no login | Jarvis (próxima versão) |

---

*Toledo Digital · Este documento é confidencial · Atualizar após cada projeto entregue*
