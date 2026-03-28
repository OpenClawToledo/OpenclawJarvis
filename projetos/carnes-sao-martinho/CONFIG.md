# CONFIG — Carnes São Martinho
> Valores específicos deste cliente para o application.properties

```properties
server.port=8083
app.name=Carnes São Martinho
app.url=https://carnessaomartinho.pt
admin.email=geral@carnessaomartinho.pt

feature.b2b=true
feature.weight.pricing=true
feature.allergens=true
feature.delivery=true
feature.pickup=true
feature.instagram=false

b2b.min.order.kg=5
b2b.default.discount.percent=15
delivery.free.above=50.00
delivery.cost=5.00
```

## Módulos a instalar
- [x] Weight Pricing
- [x] Allergens
- [x] B2B (se pacote €1.800+)

## Pendente (preencher após Reunião 1)
- `app.whatsapp` — número WhatsApp Business da loja
- `easypay.api.id` + `easypay.api.key` — gateway pagamentos
- `admin.secret` — gerar novo secret seguro
- `jwt.secret` — gerar novo secret seguro

## Categorias a criar (seed)
Bovino | Suíno | Aves | Caprino | Coelho | Fumados | Congelados | Preparados | Mercearia
