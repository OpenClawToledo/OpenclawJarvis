<template>
  <div id="fiosmj-app">
    <AppHeader @open-cart="cartOpen = true" />
    <HeroSection />
    <ProductGrid :products="products" />
    <HowToOrder />
    <AboutSection />
    <AppFooter />
    <WhatsAppFloat />

    <!-- Cart Drawer -->
    <CartDrawer
      :open="cartOpen"
      @close="cartOpen = false"
      @checkout="openCheckout"
    />

    <!-- Checkout Form -->
    <CheckoutForm
      v-if="checkoutOpen"
      @close="checkoutOpen = false"
    />
  </div>
</template>

<script>
import AppHeader from './components/AppHeader.vue'
import HeroSection from './components/HeroSection.vue'
import ProductGrid from './components/ProductGrid.vue'
import HowToOrder from './components/HowToOrder.vue'
import AboutSection from './components/AboutSection.vue'
import AppFooter from './components/AppFooter.vue'
import WhatsAppFloat from './components/WhatsAppFloat.vue'
import CartDrawer from './components/CartDrawer.vue'
import CheckoutForm from './components/CheckoutForm.vue'

export default {
  name: 'App',
  components: {
    AppHeader,
    HeroSection,
    ProductGrid,
    HowToOrder,
    AboutSection,
    AppFooter,
    WhatsAppFloat,
    CartDrawer,
    CheckoutForm
  },
  data() {
    return {
      products: [],
      cartOpen: false,
      checkoutOpen: false
    }
  },
  methods: {
    openCheckout() {
      this.cartOpen = false
      this.checkoutOpen = true
    }
  },
  async mounted() {
    try {
      const res = await fetch('/api/products')
      this.products = await res.json()
    } catch (e) {
      // Fallback products if API is not available
      this.products = [
        {
          id: 1,
          name: 'Cropped Halter Brasil 🇧🇷',
          description: 'Cropped de crochê com tema Copa do Mundo 2026! Feito à mão com fio 100% algodão nas cores da bandeira do Brasil.',
          price: 100.0,
          imageUrl: '/img/cropped-brasil.jpg',
          category: 'Roupas',
          sizes: [
            { size: 'P', price: 100 },
            { size: 'M', price: 120 },
            { size: 'G', price: 150 }
          ]
        },
        {
          id: 2,
          name: 'Amigurumi Nossa Senhora 🙏',
          description: 'Amigurumi artesanal da Nossa Senhora Aparecida, feito com muito carinho e devoção. Detalhes em dourado.',
          price: 80.0,
          imageUrl: '/img/nossa-senhora.jpg',
          category: 'Amigurumi',
          sizes: null
        },
        {
          id: 3,
          name: 'Caneta Decorada ✏️',
          description: 'Caneta decorada com crochê artesanal colorido. Ótima opção de presente criativo e único!',
          price: 20.0,
          imageUrl: '/img/caneta.jpg',
          category: 'Acessórios',
          sizes: null
        }
      ]
    }
  }
}
</script>
