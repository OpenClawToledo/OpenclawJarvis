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
      <button class="menu-toggle" @click="menuOpen = !menuOpen" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>
</template>

<script>
export default {
  name: 'AppHeader',
  data() {
    return { menuOpen: false }
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

@media (max-width: 768px) {
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
  }

  .nav.open {
    transform: translateY(0);
  }

  .nav a {
    font-size: 1.1rem;
  }
}
</style>
