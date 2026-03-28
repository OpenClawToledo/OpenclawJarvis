#!/bin/bash
# Toledo Commerce — Novo Projeto de Cliente
# Uso: bash new-client.sh [nome-cliente] [porta] [pacote]
# Ex:  bash new-client.sh carnes-sm 8083 carnessm

CLIENT=$1
PORT=$2
PACKAGE=$3
BASE="/data/.openclaw/workspace"

if [ -z "$CLIENT" ] || [ -z "$PORT" ] || [ -z "$PACKAGE" ]; then
  echo "Uso: bash new-client.sh [nome-cliente] [porta] [pacote-java]"
  exit 1
fi

echo "🚀 Criando projeto: $CLIENT (porta $PORT)"

# 1. Clone da base
cp -r "$BASE/fiosmj-app" "$BASE/$CLIENT-app"
echo "✅ Base copiada"

# 2. Renomear pacotes Java
find "$BASE/$CLIENT-app/src" -name "*.java" | while read f; do
  sed -i "s/com\.fiosmj\.app/com.toledodigital.$PACKAGE/g" "$f"
  sed -i "s/FiosMjApplication/${PACKAGE^}Application/g" "$f"
done
echo "✅ Pacotes renomeados"

# 3. Renomear pasta de pacote
OLD_PKG="$BASE/$CLIENT-app/src/main/java/com/fiosmj/app"
NEW_PKG="$BASE/$CLIENT-app/src/main/java/com/toledodigital/$PACKAGE"
mkdir -p "$(dirname "$NEW_PKG")"
mv "$OLD_PKG" "$NEW_PKG"
echo "✅ Estrutura de pastas atualizada"

# 4. Config inicial
cp "$BASE/toledo-commerce-template/client.properties.example" \
   "$BASE/$CLIENT-app/src/main/resources/application.properties"
sed -i "s/\[CLIENTE\]/$CLIENT/g" "$BASE/$CLIENT-app/src/main/resources/application.properties"
sed -i "s/808X/$PORT/g" "$BASE/$CLIENT-app/src/main/resources/application.properties"
echo "✅ application.properties gerado — preencher campos [...]"

# 5. Limpar DB e uploads do projeto anterior
rm -f "$BASE/$CLIENT-app/fiosmj.db"
rm -rf "$BASE/$CLIENT-app/uploads/instagram"
mkdir -p "$BASE/$CLIENT-app/uploads/products"
echo "✅ DB e uploads limpos"

echo ""
echo "📁 Projeto criado em: $BASE/$CLIENT-app"
echo "📝 Próximo passo: editar application.properties com dados do cliente"
echo "📦 Módulos disponíveis: $BASE/toledo-commerce-template/modules/"
echo "🔨 Build: cd $BASE/$CLIENT-app && mvn package -DskipTests"
