# HEARTBEAT.md

## Rastreio de itens da Maju — Fios MJ

Se recebeste mensagens do grupo Openclaw (120363409073908907@g.us) com IMAGENS ou descrições de produtos novos da Maju:

1. Lê /data/.openclaw/workspace/memory/maju-product-counter.json
2. Adiciona o número de novos itens detectados ao pending_count; actualiza items[] e last_updated
3. Guarda o ficheiro
4. NÃO notificas Toledo — o cron horário verifica e actua quando pending_count >= 3

Se não houver mensagens novas da Maju com produtos: HEARTBEAT_OK
