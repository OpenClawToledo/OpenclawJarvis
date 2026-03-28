# Projectos de Software — Toledo Dev

## Clientes Activos

| Projecto | Cliente | Estado | Valor | Pasta |
|---|---|---|---|---|
| Mar de Prata — App QR Code | Filha Sr. Song (+351 966 599 195) | Proposta enviada | €550 | mar-de-prata/ |
| Gabinete Contabilidade | Filha Sr. Song (+351 966 599 195) | Proposta enviada | €600 | gabinete-contabilidade/ |

**Total proposto:** €1.150 | **Pagamento:** integral na entrega, sem adiantamento

## Estrutura de cada projecto

```
projetos/
└── nome-projecto/
    ├── REQUISITOS.md     ← levantamento, decisões, fases, acessos
    ├── CONTRATO.md       ← quando formalizado (opcional)
    └── NOTAS.md          ← log de reuniões e decisões durante produção
```

## Git — Política

Cada projecto tem o seu próprio repositório privado no GitHub.
- `main` → produção (VPS do cliente)
- `develop` → desenvolvimento local
- Deploy via SSH + git pull no VPS do cliente

## VPS — Política

Cada cliente tem o seu próprio VPS no Hostinger.
- Cliente cria e paga conta Hostinger
- Toledo recebe acesso SSH temporário para setup e deploy
- Credenciais ficam registadas em REQUISITOS.md (secção 7)
- Após entrega, acesso SSH pode ser revogado pelo cliente
