<template>
  <section id="sobre" class="about-section">
    <div class="container">
      <div class="about-inner">
        <div class="about-content">
          <h2 class="section-title" style="text-align: left;">💗 Sobre a Fios MJ</h2>
          <p class="about-text">
            Somos <strong>mãe e filha</strong> unidas pela paixão pelo crochê! 🧶 Cada peça que criamos 
            carrega carinho, dedicação e muitas horas de trabalho manual.
          </p>
          <p class="about-text">
            Trabalhamos com encomendas personalizadas — você escolhe as cores, o tamanho e o modelo. 
            Do amigurumi fofo à roupa estilosa, a gente faz com amor!
          </p>
          <p class="about-text">
            ✨ <em>Crochê artesanal feito com o coração</em>
          </p>
          <div class="about-stats">
            <div class="stat">
              <span class="stat-number">100+</span>
              <span class="stat-label">Peças entregues</span>
            </div>
            <div class="stat">
              <span class="stat-number">💯</span>
              <span class="stat-label">Feito à mão</span>
            </div>
            <div class="stat">
              <span class="stat-number">🇧🇷</span>
              <span class="stat-label">Envio nacional</span>
            </div>
          </div>
          <div class="about-social">
            <a href="https://instagram.com/fiosmjcroche" target="_blank" rel="noopener" class="btn-pink">
              📸 Siga no Instagram — @fiosmjcroche
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default { name: 'AboutSection' }
</script>

<style scoped>
.about-section {
  padding: 80px 0;
  background: linear-gradient(135deg, var(--pink-light) 0%, #fff 100%);
}

.about-content {
  max-width: 700px;
}

.about-text {
  color: var(--text-dark);
  font-size: 1.1rem;
  margin-bottom: 16px;
  line-height: 1.7;
}

.about-stats {
  display: flex;
  gap: 40px;
  margin: 30px 0;
}

.stat {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat-number {
  font-size: 2rem;
  font-weight: 700;
  color: var(--pink-primary);
  font-family: 'Playfair Display', serif;
}

.stat-label {
  font-size: 0.85rem;
  color: var(--text-light);
  margin-top: 4px;
}

.about-social {
  margin-top: 24px;
}

@media (max-width: 768px) {
  .about-section {
    padding: 50px 0;
  }

  .section-title {
    text-align: center !important;
  }

  .about-stats {
    justify-content: center;
    gap: 24px;
  }

  .about-social {
    text-align: center;
  }
}
</style>
