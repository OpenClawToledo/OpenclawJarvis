<template>
  <teleport to="body">
    <!-- Overlay -->
    <transition name="fade">
      <div v-if="open" class="cart-overlay" @click="$emit('close')"></div>
    </transition>

    <!-- Drawer -->
    <transition name="slide">
      <div v-if="open" class="cart-drawer">
        <!-- Header -->
        <div class="drawer-header">
          <h2 class="drawer-title">🛒 Meu Carrinho <span class="cart-count">({{ count }} {{ count === 1 ? 'item' : 'itens' }})</span></h2>
          <button class="btn-close" @click="$emit('close')" aria-label="Fechar">✕</button>
        </div>

        <!-- Empty state -->
        <div v-if="items.length === 0" class="cart-empty">
          <span class="empty-icon">🛍️</span>
          <p>Seu carrinho está vazio.</p>
          <p class="empty-sub">Adicione produtos lindos da Maju! 🧶</p>
        </div>

        <!-- Items list -->
        <div v-else class="cart-items">
          <div v-for="item in items" :key="item.key" class="cart-item">
            <img
              :src="item.product.imageUrl"
              :alt="item.product.name"
              class="item-image"
            />
            <div class="item-details">
              <p class="item-name">{{ item.product.name }}</p>
              <p v-if="item.selectedSize" class="item-size">Tamanho: {{ item.selectedSize.size }}</p>
              <p class="item-price">R$ {{ item.price.toFixed(2).replace('.', ',') }} un.</p>
            </div>
            <div class="item-qty">
              <button class="qty-btn" @click="updateQty(item.key, -1)">−</button>
              <span class="qty-value">{{ item.quantity }}</span>
              <button class="qty-btn" @click="updateQty(item.key, 1)">+</button>
            </div>
            <button class="btn-remove" @click="removeItem(item.key)" aria-label="Remover">🗑</button>
          </div>
        </div>

        <!-- Footer -->
        <div v-if="items.length > 0" class="drawer-footer">
          <div class="cart-total">
            <span>Total:</span>
            <span class="total-value">R$ {{ total.toFixed(2).replace('.', ',') }}</span>
          </div>
          <button class="btn-checkout" @click="$emit('checkout')">
            Finalizar Compra →
          </button>
        </div>
      </div>
    </transition>
  </teleport>
</template>

<script>
import { useCart } from '../store/cart.js'

export default {
  name: 'CartDrawer',
  props: {
    open: { type: Boolean, default: false }
  },
  emits: ['close', 'checkout'],
  setup() {
    const { items, removeItem, updateQty, total, count } = useCart()
    return { items, removeItem, updateQty, total, count }
  }
}
</script>

<style scoped>
.cart-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 999;
}

.cart-drawer {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  width: 380px;
  max-width: 100vw;
  background: white;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  box-shadow: -4px 0 30px rgba(0, 0, 0, 0.15);
}

.drawer-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 24px;
  border-bottom: 2px solid #fce4f0;
  background: #fff5fb;
}

.drawer-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: #e91e7b;
  margin: 0;
}

.cart-count {
  font-size: 0.9rem;
  color: #888;
  font-weight: 400;
}

.btn-close {
  background: none;
  border: none;
  font-size: 1.2rem;
  cursor: pointer;
  color: #999;
  padding: 4px 8px;
  border-radius: 6px;
  transition: background 0.2s;
}

.btn-close:hover {
  background: #f0f0f0;
  color: #555;
}

/* Empty state */
.cart-empty {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 40px;
  color: #aaa;
  text-align: center;
}

.empty-icon {
  font-size: 3rem;
}

.empty-sub {
  font-size: 0.85rem;
  color: #ccc;
}

/* Items */
.cart-items {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.cart-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  border: 1px solid #f5e0ec;
  border-radius: 12px;
  background: #fffafd;
}

.item-image {
  width: 60px;
  height: 60px;
  object-fit: cover;
  border-radius: 8px;
  flex-shrink: 0;
}

.item-details {
  flex: 1;
  min-width: 0;
}

.item-name {
  font-size: 0.9rem;
  font-weight: 600;
  color: #333;
  margin: 0 0 2px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.item-size {
  font-size: 0.78rem;
  color: #e91e7b;
  margin: 0 0 2px;
}

.item-price {
  font-size: 0.82rem;
  color: #888;
  margin: 0;
}

.item-qty {
  display: flex;
  align-items: center;
  gap: 6px;
}

.qty-btn {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: 2px solid #e91e7b;
  background: white;
  color: #e91e7b;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s, color 0.2s;
  flex-shrink: 0;
}

.qty-btn:hover {
  background: #e91e7b;
  color: white;
}

.qty-value {
  font-weight: 700;
  font-size: 1rem;
  min-width: 20px;
  text-align: center;
}

.btn-remove {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  opacity: 0.5;
  transition: opacity 0.2s;
  flex-shrink: 0;
  padding: 4px;
}

.btn-remove:hover {
  opacity: 1;
}

/* Footer */
.drawer-footer {
  border-top: 2px solid #fce4f0;
  padding: 20px 24px;
  background: #fff5fb;
}

.cart-total {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  font-size: 1.1rem;
  font-weight: 600;
  color: #333;
}

.total-value {
  font-size: 1.4rem;
  font-weight: 700;
  color: #e91e7b;
  font-family: 'Playfair Display', serif;
}

.btn-checkout {
  width: 100%;
  padding: 14px;
  background: #e91e7b;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  transition: opacity 0.2s, transform 0.1s;
  font-family: inherit;
}

.btn-checkout:hover {
  opacity: 0.9;
  transform: translateY(-1px);
}

/* Transitions */
.fade-enter-active,
.fade-leave-active { transition: opacity 0.3s ease; }
.fade-enter-from,
.fade-leave-to { opacity: 0; }

.slide-enter-active,
.slide-leave-active { transition: transform 0.3s ease; }
.slide-enter-from,
.slide-leave-to { transform: translateX(100%); }
</style>
