#!/bin/bash
# deploy.sh — Fios MJ
# Uso: ./deploy.sh
# Pré-requisito: .env preenchido, Docker + Docker Compose instalados

set -e

echo "🚀 [deploy] Iniciando deploy Fios MJ..."

# 1. Puxar última versão do Git
echo "📥 [deploy] git pull..."
git pull origin main

# 2. Build da nova imagem
echo "🔨 [deploy] docker build..."
docker-compose build --no-cache backend

# 3. Subir com zero downtime (recria só o backend)
echo "♻️  [deploy] reiniciando containers..."
docker-compose up -d --force-recreate backend

# 4. Verificar se subiu
sleep 8
STATUS=$(docker inspect --format='{{.State.Health.Status}}' fiosmj-backend 2>/dev/null || echo "running")
HTTP=$(curl -s -o /dev/null -w "%{http_code}" http://localhost/api/products 2>/dev/null || echo "000")

if [ "$HTTP" = "200" ]; then
  echo "✅ [deploy] OK — app a responder (HTTP $HTTP)"
else
  echo "❌ [deploy] ERRO — app não responde (HTTP $HTTP)"
  echo "Logs:"
  docker-compose logs --tail=30 backend
  exit 1
fi

echo "🎉 [deploy] Deploy concluído!"
