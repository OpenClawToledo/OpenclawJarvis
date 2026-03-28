# Toledo Commerce Template
> Base reutilizável para qualquer projeto de comércio digital
> SolutionSoftware — Jarvis executa, Toledo fecha.

---

## O que é

O `fiosmj-app` é a base comprovada de todos os projetos de comércio da SolutionSoftware.
Contém: Spring Boot + Vue.js + SQLite + JWT + Cart + Checkout + Orders + Auth + Image Upload.

Para cada novo cliente: **clone + configure + adicione módulos** conforme o nicho.

---

## Como criar um projeto novo

```bash
# 1. Clone a base (fiosmj-app é o template vivo)
cp -r /data/.openclaw/workspace/fiosmj-app /data/.openclaw/workspace/[cliente]-app

# 2. Renomeia o pacote Java
cd [cliente]-app
find src -name "*.java" | xargs sed -i 's/com.fiosmj.app/com.toledodigital.[cliente]/g'
find src -name "*.java" | xargs sed -i 's/FiosMjApplication/[Cliente]Application/g'

# 3. Configura application.properties (ver client.properties.example)
cp /data/.openclaw/workspace/toledo-commerce-template/client.properties.example \
   src/main/resources/application.properties

# 4. Adiciona módulos conforme o nicho (ver /modules/)

# 5. Build e deploy
export JAVA_HOME=/home/linuxbrew/.linuxbrew/opt/openjdk
mvn package -DskipTests
nohup java -jar target/[cliente]-app-1.0.0.jar --server.port=[PORTA] &
```

---

## Módulos disponíveis

| Módulo | Quando usar | Pasta |
|---|---|---|
| **B2B** | Talhos, grossistas, fornecedores | `modules/b2b/` |
| **Weight Pricing** | Talhos, mercearias (preço/kg) | `modules/weight-pricing/` |
| **Allergens** | Restauração, alimentação | `modules/allergens/` |

### Adicionar um módulo
```bash
# Copiar os ficheiros do módulo para o projeto
cp -r /data/.openclaw/workspace/toledo-commerce-template/modules/b2b/java/* \
      [cliente]-app/src/main/java/com/toledodigital/[cliente]/

# Ajustar package nas classes copiadas
find [cliente]-app/src -name "*.java" | xargs sed -i \
  's/package com.toledodigital.carnessm/package com.toledodigital.[cliente]/g'
```

---

## Portas por projeto

| Projeto | Porta | Estado |
|---|---|---|
| Fios MJ | 8081 | ✅ live |
| BabyCloset | 8082 | ✅ live |
| Carnes São Martinho | 8083 | 🔵 aguarda negócio |
| Mar de Prata QR | 8084 | 🔵 aguarda negócio |
| Gabinete Contabilidade | 8085 | 🔵 aguarda negócio |
| Próximo cliente | 8086+ | — |

---

## O que já vem na base (fiosmj-app)

✅ Product (CRUD, imagens, categorias, SEO)
✅ Order + OrderItem
✅ Customer (registo, login, histórico)
✅ Cart + SavedCart (carrinho abandonado)
✅ Checkout + pagamento MercadoPago/Easypay
✅ Auth JWT (JwtUtil + JwtAuthFilter)
✅ SecurityConfig + WebConfig + CORS
✅ ImageProxyController (upload + download de imagens)
✅ NotificationService (WhatsApp via OpenClaw)
✅ AbandonedCartScheduler (recuperação de carrinhos)
✅ SocialController (Instagram posts, depoimentos)
✅ StatsController
✅ Vue.js 3 + Vite + Pinia + Vue Router

## O que NÃO vem na base (adicionar por módulo)

❌ B2B: Company, OrderTemplate, Invoice, B2BController
❌ Weight-based pricing (preço por kg com slider)
❌ 14 alergénios por produto
❌ Geração de PDF (faturas mensais)

---

## Tempo estimado por tipo de projeto

| Tipo | Módulos a adicionar | Dias de trabalho |
|---|---|---|
| Loja online padrão | nenhum (base suficiente) | 3–5 dias |
| Talho / mercearia B2C | Weight Pricing + Allergens | 5–7 dias |
| Talho com portal B2B | Weight Pricing + Allergens + B2B | 8–12 dias |
| Restaurante (só QR) | QR Orders (ver mar-de-prata) | 5–8 dias |
