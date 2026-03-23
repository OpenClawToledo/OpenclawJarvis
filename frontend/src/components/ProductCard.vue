<template>
  <div class="product-card">
    <div class="product-image-wrap">
      <img :src="product.imageUrl" :alt="product.name" class="product-image" loading="lazy" />
      <span class="product-category">{{ product.category }}</span>
    </div>
    <div class="product-info">
      <h3 class="product-name">{{ product.name }}</h3>
      <p class="product-desc">{{ product.description }}</p>

      <!-- Sizes display -->
      <div v-if="product.sizes && product.sizes.length" class="product-sizes">
        <span v-for="s in product.sizes" :key="s.size" class="size-badge">
          {{ s.size }} — R${{ s.price.toFixed(0) }}
        </span>
      </div>
      <div v-else class="product-price">
        R$ {{ product.price.toFixed(2).replace('.', ',') }}
      </div>

      <!-- Size selector for products with sizes (checkout) -->
      <div v-if="product.sizes && product.sizes.length" class="size-select-wrap">
        <label class="size-select-label">Tamanho para compra:</label>
        <select v-model="selectedSize" class="size-select">
          <option value="" disabled>Selecione o tamanho</option>
          <option v-for="s in product.sizes" :key="s.size" :value="s">
            {{ s.size }} — R${{ s.price.toFixed(2).replace('.', ',') }}
          </option>
        </select>
      </div>

      <!-- WhatsApp button -->
      <a :href="whatsappUrl" target="_blank" rel="noopener" class="btn-whatsapp btn-order">
        💬 Pedir pelo WhatsApp
      </a>

      <!-- Buy now button -->
      <button
        class="btn-buy btn-order"
        :disabled="loading"
        @click="handleBuy"
      >
        {{ loading ? 'Processando...' : '🛒 Comprar agora' }}
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProductCard',
  props: {
    product: { type: Object, required: true }
  },
  data() {
    return {
      loading: false,
      selectedSize: ''
    }
  },
  computed: {
    whatsappUrl() {
      const name = this.product.name.replace(/[\u{1F000}-\u{1FFFF}]/gu, '').trim()
      const msg = encodeURIComponent(`Olá! Tenho interesse no produto: ${name}. Pode me dar mais informações? 🧶`)
      return `https://wa.me/5533999892409?text=${msg}`
    },
    checkoutPrice() {
      if (this.product.sizes && this.product.sizes.length) {
        return this.selectedSize ? this.selectedSize.price : null
      }
      return this.product.price
    }
  },
  methods: {
    async handleBuy() {
      // Validate size selection
      if (this.product.sizes && this.product.sizes.length && !this.selectedSize) {
        alert('Por favor, selecione um tamanho antes de continuar.')
        return
      }

      this.loading = true
      try {
        const response = await fetch('/api/checkout/preference', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            productId: this.product.id,
            productName: this.product.name,
            price: this.checkoutPrice,
            quantity: 1
          })
        })

        if (!response.ok) {
          throw new Error(`Erro ${response.status}: ${response.statusText}`)
        }

        const data = await response.json()
        if (data.init_point) {
          window.location.href = data.init_point
        } else {
          throw new Error(data.error || 'Resposta inválida do servidor')
        }
      } catch (err) {
        alert('Erro ao processar pagamento: ' + err.message)
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.product-card {
  background: white;
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: var(--transition);
}

.product-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow-hover);
}

.product-image-wrap {
  position: relative;
  overflow: hidden;
  aspect-ratio: 1;
}

.product-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}

.product-card:hover .product-image {
  transform: scale(1.05);
}

.product-category {
  position: absolute;
  top: 12px;
  right: 12px;
  background: var(--pink-primary);
  color: white;
  padding: 4px 14px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
}

.product-info {
  padding: 20px;
}

.product-name {
  font-size: 1.3rem;
  color: var(--pink-dark);
  margin-bottom: 8px;
}

.product-desc {
  color: var(--text-light);
  font-size: 0.9rem;
  margin-bottom: 14px;
  line-height: 1.5;
}

.product-sizes {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 16px;
}

.size-badge {
  background: var(--pink-light);
  color: var(--pink-dark);
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
}

.product-price {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--pink-primary);
  margin-bottom: 16px;
  font-family: 'Playfair Display', serif;
}

.size-select-wrap {
  margin-bottom: 14px;
}

.size-select-label {
  display: block;
  font-size: 0.85rem;
  color: var(--text-light);
  margin-bottom: 6px;
  font-weight: 600;
}

.size-select {
  width: 100%;
  padding: 8px 12px;
  border: 2px solid var(--pink-light);
  border-radius: 8px;
  font-size: 0.9rem;
  color: var(--pink-dark);
  background: white;
  cursor: pointer;
  outline: none;
  transition: border-color 0.2s;
}

.size-select:focus {
  border-color: var(--pink-primary);
}

.btn-order {
  display: block;
  width: 100%;
  text-align: center;
  padding: 12px;
  font-size: 0.95rem;
  margin-bottom: 10px;
  border-radius: var(--radius, 8px);
  font-weight: 600;
  text-decoration: none;
  transition: opacity 0.2s, transform 0.1s;
}

.btn-whatsapp {
  background: #25d366;
  color: white;
}

.btn-whatsapp:hover {
  opacity: 0.9;
}

.btn-buy {
  background: #e91e7b;
  color: white;
  border: none;
  cursor: pointer;
  font-family: inherit;
}

.btn-buy:hover:not(:disabled) {
  opacity: 0.9;
  transform: translateY(-1px);
}

.btn-buy:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}
</style>
