# Jarvis — Toledo Digital

Ambiente completo do assistente Jarvis + apps Toledo Digital.

## Recuperação numa máquina nova

```bash
# 1. Clonar o workspace
git clone https://github.com/OpenClawToledo/OpenclawJarvis.git /data/.openclaw/workspace

# 2. Criar os segredos (preencher com os valores reais)
cp /data/.openclaw/workspace/secrets.example.sh /data/.openclaw/workspace/secrets.sh
nano /data/.openclaw/workspace/secrets.sh

# 3. Executar o bootstrap
chmod +x /data/.openclaw/workspace/bootstrap.sh
/data/.openclaw/workspace/bootstrap.sh
```

## O que está aqui

| Directório / Ficheiro | Conteúdo |
|---|---|
| `SOUL.md` | Personalidade do Jarvis |
| `MEMORY.md` | Memória de longo prazo |
| `USER.md` | Perfil do Toledo |
| `IDENTITY.md` | Identidade do assistente |
| `memory/` | Notas diárias (YYYY-MM-DD.md) |
| `propostas/` | Propostas comerciais em PDF/MD |
| `projetos/` | Requisitos e documentação por projeto |
| `scripts/` | Scripts Python (gerar PDFs, etc.) |
| `agencia/` | Templates de clientes |
| `fiosmj-app/` | App Fios MJ (porta 8081) |
| `mar-de-prata-app/` | App Mar de Prata (porta 8083) |
| `gabinete-app/` | App Gabinete de Contabilidade (porta 8084) |
| `bootstrap.sh` | Script de recuperação completo |
| `openclaw.template.json` | Template de config OpenClaw (sem segredos) |
| `secrets.example.sh` | Template de segredos (preencher localmente) |

## O que NÃO está aqui (segredos)

- `secrets.sh` — chaves de API (Anthropic, Gemini, MercadoPago)
- `openclaw.json` — configuração com tokens reais
- `*.db` — bases de dados com dados de clientes
- `.env` — variáveis de ambiente das apps

**Os segredos ficam contigo. O bootstrap monta tudo a partir deles.**

## Apps em produção

| App | Porta | Domínio |
|---|---|---|
| Fios MJ | 8081 | fiosmj.com |
| Mar de Prata | 8083 | a definir |
| Gabinete de Contabilidade | 8084 | a definir |

## Contacto

Toledo Digital · +351 931 120 429
