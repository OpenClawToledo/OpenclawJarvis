import { reactive, computed } from 'vue'

const state = reactive({ items: [] })

export function useCart() {
  const addItem = (product, quantity = 1, selectedSize = null) => {
    const price = selectedSize ? selectedSize.price : product.price
    const key = `${product.id}-${selectedSize?.size || 'default'}`
    const existing = state.items.find(i => i.key === key)
    if (existing) {
      existing.quantity += quantity
    } else {
      state.items.push({ key, product, selectedSize, price, quantity })
    }
  }

  const removeItem = (key) => {
    const idx = state.items.findIndex(i => i.key === key)
    if (idx > -1) state.items.splice(idx, 1)
  }

  const updateQty = (key, delta) => {
    const item = state.items.find(i => i.key === key)
    if (!item) return
    item.quantity += delta
    if (item.quantity <= 0) removeItem(key)
  }

  const clearCart = () => { state.items.splice(0) }

  const total = computed(() => state.items.reduce((s, i) => s + i.price * i.quantity, 0))
  const count = computed(() => state.items.reduce((s, i) => s + i.quantity, 0))

  return { items: state.items, addItem, removeItem, updateQty, clearCart, total, count }
}
