<template>
  <div class="product-card">
    <div class="product-image-wrap">
      <img :src="product.imageUrl" :alt="product.name" class="product-image" loading="lazy" />
      <span class="product-category">{{ product.category }}</span>
    </div>
    <div class="product-info">
      <h3 class="product-name">{{ product.name }}</h3>
      <p class="product-desc">{{ product.description }}</p>
      <div v-if="product.sizes && product.sizes.length" class="product-sizes">
        <span v-for="s in product.sizes" :key="s.size" class="size-badge">
          {{ s.size }} — R${{ s.price.toFixed(0) }}
        </span>
      </div>
      <div v-else class="product-price">
        R$ {{ product.price.toFixed(2).replace('.', ',') }}
      </div>
      <a :href="whatsappUrl" target="_blank" rel="noopener" class="btn-whatsapp btn-order">
        💬 Pedir pelo WhatsApp
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProductCard',
  props: {
    product: { type: Object, required: true }
  },
  computed: {
    whatsappUrl() {
      const name = this.product.name.replace(/[\u{1F000}-\u{1FFFF}]/gu, '').trim()
      const msg = encodeURIComponent(`Olá! Tenho interesse no produto: ${name}. Pode me dar mais informações? 🧶`)
      return `https://wa.me/5533999892409?text=${msg}`
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

.btn-order {
  width: 100%;
  justify-content: center;
  padding: 12px;
  font-size: 0.95rem;
}
</style>
