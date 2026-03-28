# Módulo Allergens — 14 Alergénios (Regulamento UE 1169/2011)

Obrigatório por lei para produtos alimentares com preparados.

## Os 14 alergénios

```json
["gluten","crustaceos","ovos","peixe","amendoins","soja",
 "leite","frutos_casca_rija","aipo","mostarda","sesamo",
 "dioxido_enxofre","tremocos","moluscos"]
```

## Implementação mínima

No model Product.java adicionar:

```java
@Column(columnDefinition = "TEXT")
private String allergens; // JSON array: ["gluten","leite"]
```

Na API pública, retornar `allergens` como array.
No frontend, mostrar badges coloridos por alergénio detectado.

## Labels PT para o frontend

```js
const ALLERGENS = {
  gluten: "🌾 Glúten",
  crustaceos: "🦐 Crustáceos",
  ovos: "🥚 Ovos",
  peixe: "🐟 Peixe",
  amendoins: "🥜 Amendoins",
  soja: "🫘 Soja",
  leite: "🥛 Leite/Lactose",
  frutos_casca_rija: "🌰 Frutos de casca rija",
  aipo: "🌿 Aipo",
  mostarda: "🌻 Mostarda",
  sesamo: "⚪ Sésamo",
  dioxido_enxofre: "🔴 Dióxido de Enxofre",
  tremocos: "🟡 Tremoços",
  moluscos: "🦑 Moluscos"
}
```
