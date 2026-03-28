#!/bin/bash
# ════════════════════════════════════════════════════════════════════
#  JARVIS BOOTSTRAP — SolutionSoftware
#  Recupera o ambiente completo numa máquina nova com um comando:
#
#    curl -sSL https://raw.githubusercontent.com/OpenClawToledo/OpenclawJarvis/main/bootstrap.sh | bash
#
#  Ou se já clonaste o repo:
#    chmod +x bootstrap.sh && ./bootstrap.sh
# ════════════════════════════════════════════════════════════════════
set -e

REPO="https://github.com/OpenClawToledo/OpenclawJarvis.git"
WORKSPACE="/data/.openclaw/workspace"
OPENCLAW_DIR="/data/.openclaw"

echo ""
echo "╔══════════════════════════════════════════╗"
echo "║   JARVIS BOOTSTRAP — SolutionSoftware      ║"
echo "╚══════════════════════════════════════════╝"
echo ""

# ── 1. Dependências base ─────────────────────────────────────────────
echo "→ A verificar dependências..."
command -v node >/dev/null 2>&1 || { echo "Node.js não encontrado. Instala via: https://nodejs.org"; exit 1; }
command -v java >/dev/null 2>&1 || { echo "Java não encontrado. Instala Java 21+"; exit 1; }
command -v mvn >/dev/null 2>&1  || { echo "Maven não encontrado. Instala Maven 3.8+"; exit 1; }
command -v git >/dev/null 2>&1  || { echo "Git não encontrado."; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "Python3 não encontrado."; exit 1; }
echo "   ✓ Dependências OK"

# ── 2. Instalar OpenClaw ─────────────────────────────────────────────
echo "→ A instalar OpenClaw..."
npm install -g openclaw 2>/dev/null || sudo npm install -g openclaw
echo "   ✓ OpenClaw instalado: $(openclaw --version 2>/dev/null || echo 'ok')"

# ── 3. Clonar workspace ──────────────────────────────────────────────
echo "→ A clonar workspace..."
mkdir -p "$OPENCLAW_DIR"
if [ -d "$WORKSPACE/.git" ]; then
  echo "   Workspace já existe, a actualizar..."
  cd "$WORKSPACE" && git pull origin main
else
  git clone "$REPO" "$WORKSPACE"
fi
echo "   ✓ Workspace clonado"

# ── 4. Configuração (segredos) ───────────────────────────────────────
echo ""
echo "┌─────────────────────────────────────────────┐"
echo "│  CONFIGURAÇÃO DE SEGREDOS                   │"
echo "│  (valores guardados LOCALMENTE, nunca git)  │"
echo "└─────────────────────────────────────────────┘"

if [ -f "$WORKSPACE/secrets.sh" ]; then
  echo "→ secrets.sh encontrado, a carregar..."
  source "$WORKSPACE/secrets.sh"
else
  echo "→ secrets.sh não encontrado."
  echo "  Copia secrets.example.sh para secrets.sh e preenche os valores."
  echo "  Depois corre: source secrets.sh && ./bootstrap.sh"
  echo ""
  cp "$WORKSPACE/secrets.example.sh" "$WORKSPACE/secrets.sh"
  echo "   Ficheiro criado em: $WORKSPACE/secrets.sh"
  exit 0
fi

# ── 5. Gerar openclaw.json ───────────────────────────────────────────
echo "→ A gerar openclaw.json..."
cp "$WORKSPACE/openclaw.template.json" "$OPENCLAW_DIR/openclaw.json"
# Substitui placeholders
sed -i "s/PREENCHER_ANTHROPIC_KEY/$ANTHROPIC_API_KEY/g" "$OPENCLAW_DIR/openclaw.json"
sed -i "s/PREENCHER_GEMINI_KEY/$GEMINI_API_KEY/g" "$OPENCLAW_DIR/openclaw.json"
echo "   ✓ openclaw.json gerado"

# ── 6. Gerar .env das apps ───────────────────────────────────────────
echo "→ A gerar .env das apps..."

# Fios MJ
cat > "$WORKSPACE/fiosmj-app/.env" << EOF
ADMIN_SECRET=$FIOSMJ_ADMIN_SECRET
JWT_SECRET=$FIOSMJ_JWT_SECRET
MP_ACCESS_TOKEN=$FIOSMJ_MP_ACCESS_TOKEN
MP_PUBLIC_KEY=$FIOSMJ_MP_PUBLIC_KEY
BASE_URL=http://localhost:8081
EOF

# Mar de Prata
cat > "$WORKSPACE/mar-de-prata-app/.env" << EOF
ADMIN_SECRET=$MAR_DE_PRATA_ADMIN_SECRET
BASE_URL=http://localhost:8083
EOF

# Gabinete
cat > "$WORKSPACE/gabinete-app/.env" << EOF
ADMIN_SECRET=$GABINETE_ADMIN_SECRET
BASE_URL=http://localhost:8084
EOF

echo "   ✓ Ficheiros .env gerados"

# ── 7. Build das apps ────────────────────────────────────────────────
echo "→ A compilar aplicações (pode demorar 2-3 min)..."
cd "$WORKSPACE/fiosmj-app" && mvn clean package -q -DskipTests && echo "   ✓ fiosmj-app OK"
cd "$WORKSPACE/mar-de-prata-app" && mvn clean package -q -DskipTests 2>/dev/null && echo "   ✓ mar-de-prata-app OK" || echo "   ⚠ mar-de-prata-app (ainda em desenvolvimento)"
cd "$WORKSPACE/gabinete-app" && mvn clean package -q -DskipTests 2>/dev/null && echo "   ✓ gabinete-app OK" || echo "   ⚠ gabinete-app (ainda em desenvolvimento)"

# ── 8. Instalar deps Python ──────────────────────────────────────────
echo "→ A instalar dependências Python..."
pip3 install reportlab --quiet && echo "   ✓ reportlab OK"

# ── 9. Iniciar apps ──────────────────────────────────────────────────
echo "→ A iniciar aplicações em background..."

# Fios MJ (porta 8081)
nohup java -jar "$WORKSPACE/fiosmj-app/target/fiosmj-app-1.0.0.jar" \
  --spring.datasource.url="jdbc:sqlite:$WORKSPACE/fiosmj-app/fiosmj.db" \
  > /tmp/fiosmj.log 2>&1 &
echo "   ✓ fiosmj-app iniciada (porta 8081)"

sleep 2

# ── 10. Iniciar OpenClaw ─────────────────────────────────────────────
echo "→ A iniciar OpenClaw..."
openclaw gateway start
echo "   ✓ OpenClaw iniciado"

# ── Sumário ──────────────────────────────────────────────────────────
echo ""
echo "╔══════════════════════════════════════════╗"
echo "║   ✅  JARVIS ONLINE                      ║"
echo "╠══════════════════════════════════════════╣"
echo "║  fiosmj.com    → porta 8081              ║"
echo "║  mar-de-prata  → porta 8083              ║"
echo "║  gabinete      → porta 8084              ║"
echo "║  OpenClaw      → activo                  ║"
echo "╚══════════════════════════════════════════╝"
echo ""
echo "Jarvis está online. Fala com ele no WhatsApp."
