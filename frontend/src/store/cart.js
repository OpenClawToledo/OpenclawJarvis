import { reactive, computed } from 'vue'

const state = reactive({ items: [] })

const syncToServer = async (items) => {
  const token = localStorage.getItem('fiosmj_token')
  if (!token) return
  try {
    const payload = items.map(i => ({
      productId: i.product.id,
      productName: i.product.name,
      price: i.price,
      quantity: i.quantity,
      selectedSize: i.selectedSize?.size || null
    }))
    await fetch('/api/cart', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(payload)
    })
  } catch {
    // silent fail - local cart still works
  }
}

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
    syncToServer(state.items)
  }

  const removeItem = (key) => {
    const idx = state.items.findIndex(i => i.key === key)
    if (idx > -1) state.items.splice(idx, 1)
    syncToServer(state.items)
  }

  const updateQty = (key, delta) => {
    const item = state.items.find(i => i.key === key)
    if (!item) return
    item.quantity += delta
    if (item.quantity <= 0) {
      removeItem(key)
    } else {
      syncToServer(state.items)
    }
  }

  const clearCart = () => {
    state.items.splice(0)
    const token = localStorage.getItem('fiosmj_token')
    if (token) {
      fetch('/api/cart', {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
      }).catch(() => {})
    }
  }

  const loadFromServer = async () => {
    const token = localStorage.getItem('fiosmj_token')
    if (!token) return
    // Only load server cart if local cart is empty
    if (state.items.length > 0) {
      // Local has priority — sync local to server
      syncToServer(state.items)
      return
    }
    try {
      const res = await fetch('/api/cart', {
        headers: { 'Authorization': `Bearer ${token}` }
      })
      if (!res.ok) return
      const data = await res.json()
      if (data.items && data.items.length > 0) {
        // Rebuild cart items from server data
        for (const item of data.items) {
          const product = { id: item.productId, name: item.productName, price: item.price }
          const selectedSize = item.selectedSize ? { size: item.selectedSize, price: item.price } : null
          const key = `${item.productId}-${item.selectedSize || 'default'}`
          if (!state.items.find(i => i.key === key)) {
            state.items.push({ key, product, selectedSize, price: item.price, quantity: item.quantity })
          }
        }
      }
    } catch {
      // silent fail
    }
  }

  const total = computed(() => state.items.reduce((s, i) => s + i.price * i.quantity, 0))
  const count = computed(() => state.items.reduce((s, i) => s + i.quantity, 0))

  return { items: state.items, addItem, removeItem, updateQty, clearCart, loadFromServer, total, count }
}
