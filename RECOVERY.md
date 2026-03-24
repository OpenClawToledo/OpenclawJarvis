# RECOVERY.md — Plano de Recuperação do Jarvis
**Se o VPS for apagado, reiniciado ou o container destruído — segue este guia.**

---

## 1. REPOSITÓRIO DE BACKUP

Todo o workspace está no GitHub:
```
git@github.com:OpenClawToledo/OpenclawJarvis.git
branch: main
```

Inclui:
- SOUL.md, USER.md, IDENTITY.md, MEMORY.md
- memory/ (diários)
- projetos/ (Mar de Prata, Gabinete)
- fiosmj-app/ (código completo)

---

## 2. REINSTALAR OPENCLAW NO VPS

```bash
# No VPS (76.13.41.197), como root:
curl -fsSL https://get.openclaw.ai | bash

# Ou via npm:
npm install -g openclaw
openclaw init
```

---

## 3. RESTAURAR O WORKSPACE

```bash
# Dentro do container OpenClaw:
cd /data/.openclaw/workspace
git clone git@github.com:OpenClawToledo/OpenclawJarvis.git .
# (usar a chave SSH configurada)
```

---

## 4. RECONECTAR WHATSAPP

Após OpenClaw iniciar:
1. Abrir o painel web do OpenClaw
2. Ir a Settings → WhatsApp → Connect
3. Escanear QR Code com o telemóvel do Toledo (+351 931 120 429)
4. Aguardar confirmação de ligação

---

## 5. RESTAURAR FIOS MJ

```bash
cd /data/.openclaw/workspace/fiosmj-app

# Restaurar base de dados (se não existir backup)
# DB está no repo: fiosmj.db
# Imagens Instagram: uploads/instagram/

# Rebuildar e iniciar
mvn package -DskipTests
nohup java -jar target/fiosmj-app-1.0.0.jar --server.port=8081 &
```

---

## 6. CONFIGURAR NGINX (no host)

```nginx
# /etc/nginx/sites-available/fiosmj
server {
    listen 443 ssl;
    server_name fiosmj.com www.fiosmj.com;
    
    ssl_certificate /etc/letsencrypt/live/fiosmj.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/fiosmj.com/privkey.pem;
    
    location / {
        proxy_pass http://172.18.0.2:8081;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

```bash
# Renovar SSL (expira 2026-06-19)
certbot renew
```

---

## 7. CREDENCIAIS CRÍTICAS

> ⚠️ Guardar em local seguro (não commitar no Git público)

| Item | Valor |
|---|---|
| VPS IP | 76.13.41.197 |
| Container porta | 58250 |
| App porta | 8081 |
| OpenClaw gateway port | 18789 |
| OpenClaw gateway token | T7OKk992Hs1LnjNgheRJ5MJn8VvK47vM |
| JWT secret | fiosmj-secret-key-2026-super-secure-change-in-prod |
| Admin secret | fiosmj-admin-2026 |
| MP Access Token | (ver application.properties) |
| MP Public Key | APP_USR-518808ef-1627-44b4-a82f-cc4f393ff361 |
| DB path | /data/.openclaw/workspace/fiosmj-app/fiosmj.db |
| Toledo WhatsApp | +351 931 120 429 |
| Maju WhatsApp | +55 33 9989 2409 |
| Grupo Openclaw JID | 120363409073908907@g.us |

---

## 8. VERIFICAR SE ESTÁ TUDO OK

```bash
# App Fios MJ
curl -s -o /dev/null -w "%{http_code}" https://fiosmj.com/

# API
curl -s https://fiosmj.com/api/products | python3 -c "import sys,json; print(len(json.load(sys.stdin)), 'produtos')"

# Instagram
curl -s https://fiosmj.com/api/social/instagram | python3 -c "import sys,json; print(len(json.load(sys.stdin)), 'posts')"
```

---

## 9. CONTACTO DE EMERGÊNCIA

Se precisares de ajuda para reinstalar:
- **Toledo:** +351 931 120 429 (WhatsApp)
- **Docs OpenClaw:** https://docs.openclaw.ai
- **GitHub repo:** https://github.com/OpenClawToledo/OpenclawJarvis

---

## 10. CRONS ACTIVOS (recriar se perdidos)

| Nome | Schedule | Função |
|---|---|---|
| Renovar posts Instagram | Diário 6h Brasil | Busca posts reais @fiosmjcroche |
| Vigiar resposta Maju | A cada 15 min | Detecta credenciais Brevo/MP |

```bash
# Ver crons activos:
openclaw cron list
```
