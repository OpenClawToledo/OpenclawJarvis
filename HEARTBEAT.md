# HEARTBEAT.md

## ⚠️ REGRA DE OURO — Anti-fragmentação
Sempre que houver uma decisão, confirmação, ou mudança num projecto:
1. Actualizar `memory/projects-status.md` **na hora** (fonte de verdade única)
2. Actualizar `memory/YYYY-MM-DD.md` com o log do dia
3. NÃO confiar só na memória de sessão — ela perde-se

## Rastreio de itens da Maju — Fios MJ

Se recebeste mensagens do grupo Openclaw (120363409073908907@g.us) com IMAGENS ou descrições de produtos novos da Maju:

1. Lê /data/.openclaw/workspace/memory/maju-product-counter.json
2. Adiciona o número de novos itens detectados ao pending_count; actualiza items[] e last_updated
3. Guarda o ficheiro
4. NÃO notificas Toledo — o cron horário verifica e actua quando pending_count >= 3

Se não houver mensagens novas da Maju com produtos: HEARTBEAT_OK

## ⚠️ REGRA — Posts Fios MJ (instrução do Toledo)
Quando a Maju pedir para postar qualquer produto/conteúdo no site fiosmj.com:
- NÃO pedir credenciais — já tens acesso
- Admin URL: fiosmj.com/admin
- Admin secret: 664142b996f1496b8112e20a9c5b1aed81fce0c75462669b
- Agir directamente via API ou painel admin sem perguntar a Toledo
