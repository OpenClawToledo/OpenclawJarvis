# Módulo Weight Pricing — Preço por Kg

Substitui o preço fixo por unidade pelo preço variável por peso.
Usado em: talhos, peixarias, mercearias, queijarias.

## O que muda no Product (base)

Adicionar ao model Product.java existente:

```java
private BigDecimal pricePerKg;      // substitui ou complementa o price fixo
private BigDecimal b2bPricePerKg;   // preço B2B (null = usa desconto padrão)
private BigDecimal minWeightKg;     // ex: 0.500 (500g mínimo)
private BigDecimal maxWeightKg;     // ex: 50.000 (50kg máximo)
private boolean soldByWeight = false; // false = preço fixo, true = preço/kg
```

## O que muda no OrderItem (base)

```java
private BigDecimal weightKg;        // quantidade em kg (quando soldByWeight=true)
private BigDecimal pricePerKgAt;    // snapshot do preço no momento do pedido
// subtotal = weightKg * pricePerKgAt (quando soldByWeight)
// subtotal = quantity * priceAt     (quando !soldByWeight)
```

## Frontend — slider de peso

No componente de produto, quando `soldByWeight=true`:
- Mostrar slider: 0.5kg → maxWeightKg, passo de 0.25
- Calcular subtotal em tempo real: `(peso * pricePerKg).toFixed(2)`
- Input manual de peso com validação (min/max)

## application.properties

```properties
feature.weight.pricing=true
```
