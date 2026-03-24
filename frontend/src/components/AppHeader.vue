<template>
  <header class="header">
    <div class="container header-inner">
      <a href="#" class="logo">
        <span class="logo-icon">🧶</span>
        <span class="logo-text">Fios MJ</span>
      </a>
      <nav class="nav" :class="{ open: menuOpen }">
        <a href="#produtos" @click="menuOpen = false">Produtos</a>
        <a href="#como-pedir" @click="menuOpen = false">Como Pedir</a>
        <a href="#sobre" @click="menuOpen = false">Sobre</a>
        <a href="https://instagram.com/fiosmjcroche" target="_blank" rel="noopener" class="nav-instagram">
          📸 Instagram
        </a>
      </nav>

      <!-- Search Bar -->
      <SearchBar :products="products" @select-product="$emit('open-product', $event)" class="header-search" />

      <!-- Account button -->
      <div class="account-wrap" v-if="isLoggedIn" ref="accountRef">
        <button class="account-btn" @click="dropdownOpen = !dropdownOpen">
          👤 Olá, {{ firstName }}
          <span class="chevron">▾</span>
        </button>
        <div class="dropdown" v-if="dropdownOpen" @click.stop>
          <button class="dropdown-item" @click="openOrders">📦 Meus Pedidos</button>
          <button class="dropdown-item" @click="handleLogout">🚪 Sair</button>
        </div>
      </div>
      <button v-else class="account-btn" @click="$emit('open-auth')">
        👤 Entrar
      </button>

      <!-- Cart button -->
      <button class="cart-btn" @click="$emit('open-cart')" aria-label="Abrir carrinho">
        🛒
        <span v-if="cartCount > 0" class="cart-badge">{{ cartCount > 99 ? '99+' : cartCount }}</span>
      </button>

      <button class="menu-toggle" @click="menuOpen = !menuOpen" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>
</template>

<script>
import { useCart } from '../store/cart.js'
import { useAuth } from '../store/auth.js'
import { computed } from 'vue'

import SearchBar from './SearchBar.vue'

export default {
  name: 'AppHeader',
  components: { SearchBar },
  props: {
    products: { type: Array, default: () => [] }
  },
  emits: ['open-cart', 'open-auth', 'open-orders', 'open-product'],
  setup() {
    const { count } = useCart()
    const { customer, isLoggedIn, logout } = useAuth()
    const firstName = computed(() => customer.customer?.name?.split(' ')[0] || '')
    return { cartCount: count, customer, isLoggedIn, logout, firstName }
  },
  data() {
    return {
      menuOpen: false,
      dropdownOpen: false
    }
  },
  mounted() {
    document.addEventListener('click', this.closeDropdown)
  },
  beforeUnmount() {
    document.removeEventListener('click', this.closeDropdown)
  },
  methods: {
    closeDropdown(e) {
      if (this.$refs.accountRef && !this.$refs.accountRef.contains(e.target)) {
        this.dropdownOpen = false
      }
    },
    handleLogout() {
      this.logout()
      this.dropdownOpen = false
    },
    openOrders() {
      this.dropdownOpen = false
      this.$emit('open-orders')
    }
  }
}
</script>

<style scoped>
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  box-shadow: 0 2px 20px rgba(233, 30, 123, 0.1);
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: 'Playfair Display', serif;
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--pink-primary);
}

.logo-icon {
  font-size: 2rem;
}

.nav {
  display: flex;
  align-items: center;
  gap: 30px;
}

.nav a {
  font-weight: 500;
  color: var(--text-dark);
  transition: color 0.3s;
  font-size: 0.95rem;
}

.nav a:hover {
  color: var(--pink-primary);
}

.nav-instagram {
  color: var(--pink-primary) !important;
  font-weight: 600 !important;
}

/* Account */
.account-wrap {
  position: relative;
}

.account-btn {
  background: none;
  border: 2px solid var(--pink-primary);
  border-radius: 50px;
  padding: 6px 14px;
  font-size: 0.9rem;
  cursor: pointer;
  color: var(--pink-primary);
  font-weight: 600;
  transition: background 0.2s, color 0.2s;
  font-family: inherit;
  display: flex;
  align-items: center;
  gap: 4px;
}

.account-btn:hover {
  background: var(--pink-primary);
  color: white;
}

.chevron {
  font-size: 0.75rem;
}

.dropdown {
  position: absolute;
  top: calc(100% + 8px);
  right: 0;
  background: white;
  border-radius: 10px;
  box-shadow: 0 8px 30px rgba(0,0,0,0.15);
  min-width: 160px;
  overflow: hidden;
  z-index: 200;
}

.dropdown-item {
  display: block;
  width: 100%;
  padding: 12px 16px;
  background: none;
  border: none;
  text-align: left;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
  color: #333;
  transition: background 0.2s;
  font-family: inherit;
}

.dropdown-item:hover {
  background: #fff5fb;
  color: #e91e7b;
}

/* Cart button */
.cart-btn {
  position: relative;
  background: none;
  border: 2px solid var(--pink-primary);
  border-radius: 50px;
  padding: 6px 14px;
  font-size: 1.1rem;
  cursor: pointer;
  color: var(--pink-primary);
  transition: background 0.2s, color 0.2s;
  display: flex;
  align-items: center;
  gap: 4px;
  line-height: 1;
}

.cart-btn:hover {
  background: var(--pink-primary);
  color: white;
}

.cart-badge {
  position: absolute;
  top: -8px;
  right: -8px;
  background: #e91e7b;
  color: white;
  font-size: 0.7rem;
  font-weight: 700;
  min-width: 18px;
  height: 18px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 3px;
  border: 2px solid white;
  line-height: 1;
}

.cart-btn:hover .cart-badge {
  background: white;
  color: #e91e7b;
}

.menu-toggle {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 5px;
}

.menu-toggle span {
  display: block;
  width: 25px;
  height: 3px;
  background: var(--pink-primary);
  border-radius: 3px;
  transition: var(--transition);
}

.header-search {
  flex: 0 1 240px;
}

@media (max-width: 768px) {
  .header-search { display: none; }
  .menu-toggle {
    display: flex;
  }

  .nav {
    position: fixed;
    top: 70px;
    left: 0;
    right: 0;
    background: white;
    flex-direction: column;
    padding: 20px;
    gap: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    transform: translateY(-120%);
    transition: transform 0.3s ease;
    z-index: 99;
  }

  .nav.open {
    transform: translateY(0);
  }

  .nav a {
    font-size: 1.1rem;
  }

  .account-btn span:not(.chevron) {
    display: none;
  }
}
</style>
