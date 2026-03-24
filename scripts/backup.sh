#!/bin/bash
# Backup diário do workspace e DB do Fios MJ para o GitHub
set -e

WORKSPACE="/data/.openclaw/workspace"
DATE=$(date +%Y-%m-%d)

echo "[$DATE] Iniciando backup..."

# 1. Backup da DB do Fios MJ (copiar para o workspace antes do commit)
cp "$WORKSPACE/fiosmj-app/fiosmj.db" "$WORKSPACE/fiosmj-app/fiosmj.db.bak" 2>/dev/null || true

# 2. Commit e push do workspace
cd "$WORKSPACE/fiosmj-app"
git add -A
git diff --staged --quiet || git commit -m "backup: auto-backup $DATE"
git push origin main

echo "[$DATE] Backup concluído ✅"
