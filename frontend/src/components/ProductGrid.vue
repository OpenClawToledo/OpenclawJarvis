<template>
  <section class="products-section" id="produtos">
    <div class="container">
      <p class="section-eyebrow">🧶 Feito com amor</p>
      <h2 class="section-title">Nossos Produtos</h2>
      <p class="section-subtitle">
        Peças artesanais únicas, feitas sob encomenda. Escolha a sua e encomende pelo WhatsApp!
      </p>

      <!-- Estado de carregamento -->
      <div class="loading-state" v-if="loading">
        <div class="spinner"></div>
        <p>Carregando produtos...</p>
      </div>

      <!-- Erro -->
      <div class="error-state" v-else-if="error">
        <p>⚠️ {{ error }}</p>
        <button @click="fetchProducts" class="btn-retry">Tentar novamente</button>
      </div>

      <!-- Grid de produtos -->
      <div class="products-grid" v-else>
        <ProductCard
          v-for="product in products"
          :key="product.id"
          :product="product"
        />
      </div>

      <div class="products-cta">
        <p class="products-cta-text">Não encontrou o que procura? Fazemos peças personalizadas! 💬</p>
        <a
          href="https://wa.me/5533999892409?text=Olá!%20Gostaria%20de%20solicitar%20uma%20peça%20personalizada%20de%20crochê%20😊"
          target="_blank"
          rel="noopener noreferrer"
          class="btn-primary"
        >
          💬 Pedir Personalizado
        </a>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import ProductCard from './ProductCard.vue'

const products = ref([])
const loading = ref(true)
const error = ref(null)

async function fetchProducts() {
  loading.value = true
  error.value = null
  try {
    const res = await fetch('/api/products')
    if (!res.ok) throw new Error('Erro ao carregar produtos')
    products.value = await res.json()
  } catch (e) {
    console.error(e)
    error.value = 'Não foi possível carregar os produtos. Verifique sua conexão.'
  } finally {
    loading.value = false
  }
}

onMounted(fetchProducts)
</script>

<style scoped>
.products-section {
  padding: 80px 0;
  background: var(--white);
}

.section-eyebrow {
  text-align: center;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--pink-primary);
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 8px;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 28px;
  margin-bottom: 48px;
}

/* Loading */
.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 60px 0;
  gap: 16px;
  color: var(--gray-mid);
}

.spinner {
  width: 44px;
  height: 44px;
  border: 3px solid var(--pink-light);
  border-top-color: var(--pink-primary);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Error */
.error-state {
  text-align: center;
  padding: 40px;
  color: var(--gray-mid);
}

.btn-retry {
  margin-top: 16px;
  background: var(--pink-primary);
  color: white;
  padding: 10px 24px;
  border-radius: 40px;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
  border: none;
  font-family: var(--font-body);
}

.btn-retry:hover {
  background: var(--pink-dark);
}

/* CTA */
.products-cta {
  text-align: center;
  padding: 40px;
  background: var(--pink-pale);
  border-radius: var(--radius-lg);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.products-cta-text {
  font-size: 1.05rem;
  color: var(--gray-mid);
}

@media (max-width: 640px) {
  .products-grid {
    grid-template-columns: 1fr;
  }
}
</style>
