# 🧶 Fios MJ — Loja de Crochê Artesanal

Aplicação full-stack da loja **Fios MJ** — crochê artesanal feito com amor por mãe e filha.

**Stack:** Java Spring Boot 3 (backend) + Vue.js 3 (frontend)

## 🚀 Como Rodar

### Pré-requisitos
- Java 17+ (OpenJDK)
- Node.js 18+ e npm

### 1. Build do Frontend

```bash
cd frontend
npm install
npm run build
```

O build gera os arquivos em `src/main/resources/static/`.

### 2. Rodar o Backend

```bash
# Com Maven Wrapper (recomendado)
./mvnw spring-boot:run

# Ou com Maven global
mvn spring-boot:run
```

A aplicação sobe em **http://localhost:8081**

### 3. Desenvolvimento (frontend hot-reload)

```bash
cd frontend
npm run dev
```

O Vite sobe em `http://localhost:5173` com proxy para a API em `:8081`.

## 📁 Estrutura

```
fiosmj-app/
├── pom.xml                          # Config Maven / Spring Boot
├── mvnw                             # Maven Wrapper
├── frontend/                        # Vue.js 3 + Vite
│   ├── src/
│   │   ├── App.vue
│   │   └── components/              # Componentes Vue
│   └── public/img/                  # Imagens (copiadas pro build)
└── src/main/
    ├── java/com/fiosmj/app/         # Spring Boot backend
    │   ├── FiosMjApplication.java
    │   ├── controller/
    │   ├── model/
    │   └── config/
    └── resources/
        ├── application.properties
        └── static/                  # Build output do Vue
```

## 📱 Contato

- **WhatsApp:** [+55 33 99989-2409](https://wa.me/5533999892409)
- **Instagram:** [@fiosmjcroche](https://instagram.com/fiosmjcroche)

---

© 2026 Fios MJ — Todos os direitos reservados 💗
