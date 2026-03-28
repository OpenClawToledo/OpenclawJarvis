# Requisitos — Gabinete de Contabilidade (Filha do Sr. Song)
**Cliente:** Filha do Sr. Song (+351 966 599 195)
**Tipo:** Website institucional bilingue (PT + 中文) + Portal de cliente
**Data de abertura:** 2026-03-24
**Estado:** Proposta enviada — aguarda resposta

---

## 1. IDENTIFICAÇÃO DO PROJECTO

| Campo | Valor |
|---|---|
| Nome do projecto | gabinete-contabilidade-web |
| Git repo | a criar: github.com/[toledo]/gabinete-contabilidade (privado) |
| VPS | Por conta do cliente — Hostinger |
| Domínio | A definir pelo cliente |
| Stack | Spring Boot (Java) + Vue.js + SQLite → PostgreSQL em produção |
| Pacote contratado | Essencial (€650) / Standard (€950) — a confirmar |
| Referências enviadas | agendapadrao.com · teru.pt |

---

## 2. LEVANTAMENTO DE REQUISITOS — SESSÃO 1 (Briefing)

### 2.1 Identidade e Conteúdo
- [ ] Nome do gabinete (PT e em caracteres chineses, se aplicável)
- [ ] NIF do gabinete / dados legais completos
- [ ] Logótipo (PNG/SVG, fundo transparente)
- [ ] Cores e identidade visual preferidas
- [ ] Fotografia profissional da equipa (ou apenas da titular)
- [ ] Tem morada de escritório ou trabalha remotamente?
- [ ] Faz atendimento presencial ou apenas remoto?

### 2.2 Serviços a destacar
- [ ] Contabilidade organizada / simplificada
- [ ] Fiscalidade (IRS, IRC, IVA)
- [ ] Recursos humanos e processamento de salários
- [ ] Abertura de empresas em Portugal
- [ ] Apoio a vistos e residência (comunidade chinesa)
- [ ] Consultoria financeira
- [ ] Outros? ___

### 2.3 Público-alvo
- [ ] Empresários chineses em Portugal (principal)
- [ ] Empresas portuguesas
- [ ] Particulares (IRS)
- [ ] Proporção aproximada de clientes PT vs CN?
- [ ] Precisa de versão em inglês também?

### 2.4 Comunicação e Contacto
- [ ] Tem WeChat profissional? (essencial para clientela chinesa)
- [ ] Tem LinkedIn profissional?
- [ ] Tem WhatsApp de contacto profissional?
- [ ] Prefere formulário de contacto, marcação de consulta ou ambos?
- [ ] Pretende calendário de disponibilidade online?

### 2.5 Portal de Cliente (Pacote Standard)
- [ ] Quantos clientes activos tem actualmente (estimativa)?
- [ ] Que tipo de documentos partilha com clientes? (balancetes, declarações, recibos vencimento, modelos fiscais)
- [ ] Como partilha documentos actualmente? (e-mail, WeTransfer, pen?)
- [ ] Precisa de notificações de prazos fiscais automáticas aos clientes?
- [ ] Os clientes têm perfil técnico para usar portal ou preferem simplicidade máxima?

### 2.6 Conteúdo Adicional
- [ ] Quer blog/artigos com dicas fiscais e novidades legais?
- [ ] Quer calendário fiscal visível no site (como agendapadrao.com)?
- [ ] Tem depoimentos de clientes satisfeitos para incluir?
- [ ] Quer secção de FAQ (perguntas frequentes)?

---

## 3. DECISÕES TÉCNICAS (a preencher após briefing)

| Decisão | Opção A | Opção B | Escolha |
|---|---|---|---|
| Idiomas | PT + 中文 | PT + 中文 + EN | |
| Portal de cliente | Não | Sim | |
| Upload de documentos | Não | Sim | |
| Notificações fiscais | Não | E-mail automático | |
| Hosting VPS | KVM 1 (€5.49/mês) | KVM 2 (€7.99/mês) | |
| Domínio | .pt | .com | |

---

## 4. ESTRUTURA DE PÁGINAS

```
/ ─── Home
    ├── Hero (credibilidade + CTA contacto)
    ├── Serviços (PT e 中文)
    ├── Sobre Nós / Equipa
    ├── Porquê nós? (diferenciais: bilingue, experiência CN-PT)
    ├── Depoimentos
    ├── Calendário Fiscal
    ├── Blog / Novidades fiscais
    └── Contacto (formulário + WeChat QR + WhatsApp)

/cliente ─── Portal do cliente (login)
    ├── Documentos partilhados
    ├── Prazos e notificações
    └── Mensagens com o gabinete

/privacy ─── Política de Privacidade (RGPD)
/terms   ─── Termos e Condições
```

---

## 5. ENTREGÁVEIS POR FASE

### Fase 1 — Setup (Dia 1-2)
- [ ] Criar repositório Git privado
- [ ] Configurar VPS no Hostinger (cliente cria conta)
- [ ] Registar domínio
- [ ] Configurar nginx + SSL

### Fase 2 — Desenvolvimento (Dia 3-12)
- [ ] Backend: API REST (Spring Boot)
- [ ] Modelo de dados: clientes, documentos, notificações
- [ ] Frontend: website bilingue (Vue.js com i18n)
- [ ] Portal de cliente: upload/download de documentos
- [ ] Notificações de prazos fiscais
- [ ] RGPD reforçado (dados fiscais sensíveis)

### Fase 3 — Conteúdo (Dia 10-14)
- [ ] Tradução dos textos para mandarim (cliente fornece ou valida)
- [ ] Fotografias da equipa
- [ ] Calendário fiscal PT 2026
- [ ] Primeiros artigos do blog (opcional)

### Fase 4 — Testes (Dia 15-17)
- [ ] Teste portal: upload e download de documento
- [ ] Teste idiomas: alternância PT ↔ 中文
- [ ] Teste mobile
- [ ] Revisão RGPD + OCC (Ordem dos Contabilistas Certificados)

### Fase 5 — Entrega (Dia 18-22)
- [ ] Deploy no VPS do cliente
- [ ] Formação de utilização (45 min)
- [ ] Documentação de administração
- [ ] Entrega de credenciais

---

## 6. CONTROLO DE VERSÕES (Git)

```
Repositório: github.com/[toledo]/gabinete-contabilidade (privado)
Branch main     → produção (VPS cliente)
Branch develop  → desenvolvimento
Branch feature/* → funcionalidades em curso
```

---

## 7. ACESSO AO VPS DO CLIENTE

| Item | Valor |
|---|---|
| IP VPS | A preencher |
| Utilizador SSH | A preencher |
| Domínio | A preencher |
| Porta app | 8080 |
| DB path | /srv/gabinete/data.db |
| JAR path | /srv/gabinete/app.jar |
| Nginx config | /etc/nginx/sites-enabled/gabinete |

---

## 8. NOTAS RGPD — SECTOR CONTABILIDADE

Dados fiscais e financeiros são dados sensíveis ao abrigo do RGPD e da legislação profissional contabilística. Requisitos adicionais:

- Política de retenção de dados (quantos anos guardar documentos)
- Contrato de subcontratante de dados com os clientes (DPA — Data Processing Agreement)
- Registo de actividades de tratamento (obrigatório para profissionais que tratam dados de terceiros)
- Encriptação de documentos em repouso (não apenas em trânsito)
- Backups seguros e política de recuperação

Estes documentos são responsabilidade da titular do gabinete (OCC) — o website deve facilitar, não substituir.

---

## 9. ORÇAMENTO E PAGAMENTOS

| Item | Valor | Estado |
|---|---|---|
| Proposta enviada | 2026-03-24 | ✅ |
| Pacote escolhido | A confirmar | ⏳ |
| Sinal (50%) | — | ⏳ |
| Entrega final (50%) | — | ⏳ |
| Suporte mensal | €30/mês | ⏳ |

---

## 10. NOTAS E DECISÕES

_(Preencher durante o projecto)_
- 2026-03-24: Proposta enviada. Cliente é filha do Sr. Song (Mar de Prata). Referências: agendapadrao.com e teru.pt. Perfil: contabilista a servir comunidade chinesa em PT.

---

## ACTUALIZAÇÃO — 2026-03-28

### Estado: ACEITE ✅
- Contacto: Jiaxin Song — +351 966 599 195 — jiaxinsong327@gmail.com
- Pacote: **Essencial €650** (€600 em numerário)
- Pagamento: em numerário, na entrega
- Site bilingue: PT + 中文 (mandarim)
- WeChat integrado
- Referências: agendapadrao.com e teru.pt
- Estrutura técnica base criada: `/data/.openclaw/workspace/gabinete-app/`
- Port local: 8084

### Decisões confirmadas
- Pacote Essencial: site + SEO + calendário fiscal + WeChat
- Bilingue PT/中文 desde o primeiro dia
- Acesso total ao painel admin após entrega (cliente gere sozinha)
- SQLite em desenvolvimento

### Dados em falta (Jiaxin vai enviar)
- Nome do gabinete (PT e 中文)
- Logótipo, cores, NIF
- Lista de serviços a destacar
- Foto profissional
- WeChat QR Code / ID profissional
- Domínio pretendido
- Conta Hostinger
