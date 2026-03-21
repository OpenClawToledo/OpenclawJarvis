<template>
  <section class="hero">
    <div class="container hero-inner">
      <div class="hero-content fade-in">
        <h1 class="hero-title">Fios MJ</h1>
        <p class="hero-tagline">💗 Crochê artesanal | Mãe & Filha 🧶</p>
        <p class="hero-subtitle">Peças sob encomenda feitas com amor e dedicação 🎁</p>
        <div class="hero-actions">
          <a href="#produtos" class="btn-pink">✨ Ver Produtos</a>
          <a href="https://wa.me/5533999892409?text=Olá! Vi o site e gostaria de saber mais sobre as peças de crochê 🧶" 
             target="_blank" rel="noopener" class="btn-whatsapp">
            💬 Fale Conosco
          </a>
        </div>
      </div>
      <div class="hero-decoration">
        <div class="yarn-ball">🧶</div>
      </div>
    </div>
  </section>
</template>

<script>
export default { name: 'HeroSection' }
</script>

<style scoped>
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  background: linear-gradient(135deg, var(--pink-light) 0%, var(--pink-bg) 50%, #fff 100%);
  padding-top: 70px;
  overflow: hidden;
  position: relative;
}

.hero-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
}

.hero-content {
  flex: 1;
  max-width: 600px;
}

.hero-title {
  font-size: 4rem;
  color: var(--pink-primary);
  margin-bottom: 12px;
  line-height: 1.1;
}

.hero-tagline {
  font-size: 1.4rem;
  color: var(--pink-dark);
  margin-bottom: 8px;
  font-weight: 500;
}

.hero-subtitle {
  font-size: 1.15rem;
  color: var(--text-light);
  margin-bottom: 32px;
}

.hero-actions {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

.hero-decoration {
  flex-shrink: 0;
}

.yarn-ball {
  font-size: 12rem;
  animation: pulse 3s ease-in-out infinite;
  filter: drop-shadow(0 10px 30px rgba(233, 30, 123, 0.2));
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 2.8rem;
  }

  .hero-tagline {
    font-size: 1.15rem;
  }

  .hero-inner {
    flex-direction: column;
    text-align: center;
  }

  .hero-actions {
    justify-content: center;
  }

  .yarn-ball {
    font-size: 6rem;
  }
}
</style>
