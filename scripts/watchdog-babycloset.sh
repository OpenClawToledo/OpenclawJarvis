#!/bin/bash

# Watchdog para BabyCloset
# Testa se o app está no ar e reinicia se necessário

HEALTH_URL="http://localhost:8082/"
MAX_RETRIES=2
WAIT_TIME=10

# Testa o status da aplicação
test_health() {
  curl -s -o /dev/null -w '%{http_code}' "$HEALTH_URL"
}

# Primeira verificação
STATUS=$(test_health)

if [ "$STATUS" != "200" ]; then
  # App está down, reinicia
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] BabyCloset DOWN (HTTP $STATUS) - Reiniciando..."
  
  cd /data/.openclaw/workspace/babycloset-app || exit 1
  export JAVA_HOME=/home/linuxbrew/.linuxbrew/opt/openjdk
  bash start.sh start >> /tmp/babycloset.log 2>&1 &
  
  sleep $WAIT_TIME
  
  # Verifica se subiu
  STATUS_AFTER=$(test_health)
  
  if [ "$STATUS_AFTER" = "200" ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✅ BabyCloset reiniciado com sucesso (HTTP $STATUS_AFTER)"
    exit 0
  else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ❌ BabyCloset falhou ao reiniciar (HTTP $STATUS_AFTER)"
    exit 1
  fi
else
  # App está saudável, sem ação necessária
  exit 0
fi
