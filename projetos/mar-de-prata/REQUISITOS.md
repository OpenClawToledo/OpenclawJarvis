# Requisitos — Restaurante Mar de Prata
**Cliente:** Filha do Sr. Song (+351 966 599 195)
**Tipo:** Website institucional + App de pedidos via QR Code
**Data de abertura:** 2026-03-24
**Estado:** Proposta enviada — aguarda resposta

---

## 1. IDENTIFICAÇÃO DO PROJECTO

| Campo | Valor |
|---|---|
| Nome do projecto | mar-de-prata-web |
| Git repo | a criar: github.com/[toledo]/mar-de-prata (privado) |
| VPS | Por conta do cliente — Hostinger |
| Domínio | A definir pelo cliente |
| Stack | Spring Boot (Java) + Vue.js + SQLite → PostgreSQL em produção |
| Pacote contratado | Standard (€850) / Premium (€1.300) — a confirmar |

---

## 2. LEVANTAMENTO DE REQUISITOS — SESSÃO 1 (Briefing)

### 2.1 Identidade e Conteúdo
- [ ] Nome completo do restaurante e morada
- [ ] NIF do restaurante
- [ ] Logótipo (ficheiro em PNG/SVG, fundo transparente)
- [ ] Cores preferidas / identidade visual existente
- [ ] Fotografias do espaço, pratos e equipa (mín. 10-15 fotos)
- [ ] Horários de funcionamento
- [ ] Meios de contacto (telefone, e-mail, redes sociais)
- [ ] Tem Google Maps já configurado?

### 2.2 Menu Digital
- [ ] Quantas categorias? (Entradas, Pratos principais, Sobremesas, Bebidas...)
- [ ] Quantos pratos por categoria (estimativa)?
- [ ] Tem fotografias dos pratos ou precisam ser tiradas?
- [ ] Preços já definidos?
- [ ] Pratos têm variações (tamanho, picante, etc.)?
- [ ] **Alergénios** — quem preenche a informação de alergénios por prato? (obrigatório por lei)
- [ ] Menu em português apenas ou também em inglês/chinês?

### 2.3 Reservas
- [ ] Aceita reservas? Por formulário no site, telefone, ou ambos?
- [ ] Capacidade máxima do restaurante (nº de mesas)?
- [ ] Pretende gestão de reservas ou apenas formulário de contacto?

### 2.4 App de Pedidos QR Code (Pacote Standard/Premium)
- [ ] Quantas mesas tem o restaurante?
- [ ] Cada mesa terá QR Code impresso ou em suporte físico?
- [ ] Como é a cozinha gerida actualmente? (papel, tablet, sistema próprio?)
- [ ] Onde ficará o painel da cozinha? (tablet, TV, PC fixo?)
- [ ] Pretende impressão automática de pedido na cozinha? (requer impressora de rede)
- [ ] Aceita pagamento no site ou apenas no balcão?
- [ ] Pretende notificação no telemóvel do dono quando chega pedido?

### 2.5 Infraestrutura (Pacote Premium)
- [ ] Tem computador ou tablet disponível no restaurante para o servidor local?
- [ ] Qual a operadora de internet do restaurante?
- [ ] Tem acesso ao router para configurar rede local?

---

## 3. DECISÕES TÉCNICAS (a preencher após briefing)

| Decisão | Opção A | Opção B | Escolha |
|---|---|---|---|
| Base de dados | SQLite | PostgreSQL | |
| Autenticação clientes | Sem login | Com login | |
| Pagamentos online | Não | MB Way / Multibanco | |
| Idiomas | PT | PT + EN | |
| Hosting VPS | KVM 1 (€5.49/mês) | KVM 2 (€7.99/mês) | |

---

## 4. ESTRUTURA DE PÁGINAS

```
/ ─── Home
    ├── Hero (foto + CTA reserva)
    ├── Menu (categorias + pratos)
    ├── Sobre Nós
    ├── Galeria
    ├── Reservas
    └── Contactos / Localização

/mesa/:id ─── App de pedidos (QR Code)
/cozinha   ─── Painel da cozinha (protegido)
/admin     ─── Gestão de menu e pedidos (protegido)
/privacy   ─── Política de Privacidade (RGPD)
/terms     ─── Termos e Condições
```

---

## 5. ENTREGÁVEIS POR FASE

### Fase 1 — Setup (Dia 1-2)
- [ ] Criar repositório Git privado
- [ ] Configurar VPS no Hostinger (cliente cria conta e partilha acesso)
- [ ] Registar domínio (cliente escolhe e compra)
- [ ] Configurar nginx + SSL no VPS

### Fase 2 — Desenvolvimento (Dia 3-14)
- [ ] Backend: API REST (Spring Boot)
- [ ] Base de dados: modelo de dados (menu, pedidos, reservas)
- [ ] Frontend: website institucional (Vue.js)
- [ ] App QR Code: flow mesa → cozinha
- [ ] Painel admin: gestão de menu e pedidos
- [ ] RGPD: Privacidade, Cookies, Termos

### Fase 3 — Conteúdo (Dia 10-16)
- [ ] Integrar fotos do cliente
- [ ] Preencher menu completo
- [ ] Configurar alergénios
- [ ] Configurar QR Codes por mesa

### Fase 4 — Testes (Dia 17-19)
- [ ] Teste completo no restaurante (pedido real mesa → cozinha)
- [ ] Teste mobile (iOS e Android)
- [ ] Teste sem internet (Pacote Premium)
- [ ] Revisão RGPD

### Fase 5 — Entrega (Dia 20)
- [ ] Deploy final no VPS do cliente
- [ ] Formação ao cliente (30 min)
- [ ] Documentação básica de utilização
- [ ] Entrega de credenciais (VPS, admin, domínio)

---

## 6. CONTROLO DE VERSÕES (Git)

```
Repositório: github.com/[toledo]/mar-de-prata (privado)
Branch main     → produção (VPS cliente)
Branch develop  → desenvolvimento
Branch feature/* → funcionalidades em curso
```

**Política de commits:**
- `feat:` nova funcionalidade
- `fix:` correcção de bug
- `content:` alteração de conteúdo/menu
- `deploy:` deploy para produção

---

## 7. ACESSO AO VPS DO CLIENTE

| Item | Valor |
|---|---|
| IP VPS | A preencher |
| Utilizador SSH | A preencher |
| Domínio | A preencher |
| Porta app | 8080 |
| DB path | /srv/mar-de-prata/data.db |
| JAR path | /srv/mar-de-prata/app.jar |
| Nginx config | /etc/nginx/sites-enabled/mar-de-prata |

---

## 8. ORÇAMENTO E PAGAMENTOS

| Item | Valor | Estado |
|---|---|---|
| Proposta enviada | 2026-03-24 | ✅ |
| Pacote escolhido | A confirmar | ⏳ |
| Sinal (50%) | — | ⏳ |
| Entrega final (50%) | — | ⏳ |
| Suporte mensal | €30/mês | ⏳ |

---

## 9. NOTAS E DECISÕES

_(Preencher durante o projecto)_
- 2026-03-24: Proposta enviada via WhatsApp. Cliente referenciada pelo Sr. Song.

---

## ACTUALIZAÇÃO — 2026-03-28

### Estado: CONFIRMADO ✅
- Contacto: Jiaxin Song (filha do Sr. Song) — +351 966 599 195 — jiaxinsong327@gmail.com
- Pacote: Toledo entrega **Standard completo** (€850) como brinde — cliente paga €450 pelo QR
- Pagamento: em numerário, na entrega
- Idioma do site: Português (a confirmar se também Inglês)
- Estrutura técnica base criada: `/data/.openclaw/workspace/mar-de-prata-app/`
- Port local: 8083

### Decisões confirmadas
- Pacote Standard = website institucional + App QR de pedidos
- Sem pagamento online (apenas no balcão)
- 14 alergénios incluídos (obrigatório por lei)
- WebSocket para pedidos em tempo real (cozinha)
- SQLite em desenvolvimento → dados reais do cliente em produção

### Dados em falta (aguardar Jiaxin)
- Logótipo, cores, NIF, morada, horários
- Lista de pratos com preços e alergénios
- Número de mesas
- Domínio pretendido
- Conta Hostinger
