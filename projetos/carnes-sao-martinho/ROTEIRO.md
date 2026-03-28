# ROTEIRO — Carnes São Martinho
> 8–12 dias úteis (com template Toledo Commerce)
> Base: fiosmj-app + módulos B2B + Weight Pricing + Allergens

---

## PRÉ-PROJETO
**Reunião 0** (30 min) — Abordagem + proposta + marcar Reunião 1

---

## DIA 0 — Reunião 1: Briefing + arranque (60–90 min, presencial)
- Usar REQUISITOS.md como guião
- Recolher: produtos+preços, fotos, IBAN, NIF, acessos
- Assinar acordo e definir data de entrega
- **Jarvis:** executar `bash new-client.sh carnes-sm 8083 carnessm`

---

## DIAS 1–2 — Setup e dados
- [ ] Executar script new-client.sh → projeto base criado em minutos
- [ ] Preencher application.properties com dados do cliente
- [ ] Adicionar módulos: Weight Pricing + Allergens + B2B (se contratado)
- [ ] Seed de categorias via API
- [ ] Inserir produtos com fotos e preços

---

## DIAS 3–5 — Frontend: loja B2C
- [ ] Adaptar tema/cores da marca (CSS variables)
- [ ] Página de produto com slider de peso + cálculo em tempo real
- [ ] Alergénios visíveis por produto
- [ ] Fluxo de checkout adaptado (peso → total → pagamento)
- [ ] Confirmação por WhatsApp automático

---

## DIAS 6–8 — Portal B2B (se pacote €1.800+)
- [ ] Registo de empresa + aprovação admin
- [ ] Catálogo com preços por grosso
- [ ] Templates de pedido recorrente
- [ ] Histórico e faturas mensais PDF

---

## DIA 9 — Painel admin + SEO
- [ ] Verificar painel admin (herdado da base — já funciona)
- [ ] SEO: meta tags, sitemap, robots.txt, Open Graph
- [ ] Google Meu Negócio + WhatsApp Business

---

## DIA 10 — Reunião 2: Revisão com cliente (45 min)
- Demo completa do sistema
- Recolher feedback e lista de ajustes
- Confirmar conteúdo (produtos, textos, fotos)

---

## DIAS 11–12 — Ajustes + deploy final
- [ ] Aplicar feedback da Reunião 2
- [ ] Testes B2C e B2B (mobile iOS + Android)
- [ ] RGPD: política privacidade, cookies
- [ ] SSL no domínio final
- [ ] Deploy produção + Nginx

---

## DIA 12 — Reunião 3: Entrega + formação (60 min, presencial)
- Demo final no ar
- Formação: como gerir produtos, ver pedidos, aprovar empresas B2B
- Entregar credenciais de admin
- Receber pagamento
- Apresentar proposta de gestão mensal (€200–350/mês)

---

## Ganho do template: -3 dias vs desenvolvimento do zero

| Sem template | Com template |
|---|---|
| Setup Spring Boot: 1 dia | Setup: 15 min (script) |
| Auth/JWT/Security: 1 dia | Já incluído na base |
| Cart/Checkout: 1–2 dias | Já incluído na base |
| Upload imagens: 0.5 dia | Já incluído na base |
| **Total extra: ~3–4 dias** | **Total extra: 0** |
