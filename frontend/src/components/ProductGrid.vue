<template>
  <section id="produtos" class="products-section">
    <div class="container">
      <h2 class="section-title">✨ Nossos Produtos</h2>
      <p class="section-subtitle">Peças artesanais únicas, feitas sob encomenda com muito carinho</p>

      <div class="products-grid">
        <ProductCard
          v-for="product in products"
          :key="product.id"
          :product="product"
        />
      </div>

      <div class="products-cta">
        <p>Não encontrou o que procura? Fazemos peças personalizadas! 💬</p>
        <a
          href="https://wa.me/5533999892409?text=Olá! Gostaria de solicitar uma peça personalizada de crochê 😊"
          target="_blank"
          rel="noopener"
          class="btn-pink"
        >
          💬 Pedir Personalizado
        </a>
      </div>
    </div>
  </section>
</template>

<script>
import ProductCard from './ProductCard.vue'

export default {
  name: 'ProductGrid',
  components: { ProductCard },
  props: {
    products: { type: Array, default: () => [] }
  }
}
</script>

<style scoped>
.products-section {
  padding: 80px 0;
  background: var(--pink-bg);
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 30px;
  margin-bottom: 40px;
}

.products-cta {
  text-align: center;
  padding: 30px;
  background: var(--pink-light);
  border-radius: var(--radius);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.products-cta p {
  font-size: 1.05rem;
  color: var(--text-light);
}

@media (max-width: 768px) {
  .products-section {
    padding: 50px 0;
  }

  .products-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
}
</style>
