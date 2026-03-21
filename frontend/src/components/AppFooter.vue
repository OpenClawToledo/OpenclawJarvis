<template>
  <footer class="footer">
    <div class="container footer-inner">
      <div class="footer-brand">
        <div class="footer-logo">
          <span>🧶</span>
          <span class="footer-logo-name">Fios MJ</span>
        </div>
        <p class="footer-bio">
          💗 Crochê artesanal | Mãe &amp; Filha<br />
          🧶 Peças sob encomenda 🎁
        </p>
        <div class="footer-socials">
          <a
            href="https://www.instagram.com/fiosmjcroche"
            target="_blank"
            rel="noopener noreferrer"
            class="social-link instagram"
          >
            📸 Instagram
          </a>
          <a
            href="https://wa.me/5533999892409"
            target="_blank"
            rel="noopener noreferrer"
            class="social-link whatsapp"
          >
            💬 WhatsApp
          </a>
        </div>
      </div>

      <div class="footer-links">
        <h4>Navegação</h4>
        <ul>
          <li><a href="#inicio">Início</a></li>
          <li><a href="#produtos">Produtos</a></li>
          <li><a href="#como-pedir">Como Pedir</a></li>
          <li><a href="#sobre">Sobre Nós</a></li>
        </ul>
      </div>

      <div class="footer-contact">
        <h4>Contato</h4>
        <ul>
          <li>
            <a
              href="https://wa.me/5533999892409"
              target="_blank"
              rel="noopener noreferrer"
            >
              💬 (33) 99989-2409
            </a>
          </li>
          <li>
            <a
              href="https://www.instagram.com/fiosmjcroche"
              target="_blank"
              rel="noopener noreferrer"
            >
              📸 @fiosmjcroche
            </a>
          </li>
          <li>🇧🇷 Minas Gerais, Brasil</li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="container">
        <p>© 2026 Fios MJ · Crochê Artesanal · Feito com 💗</p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background: var(--gray-dark);
  color: rgba(255, 255, 255, 0.85);
}

.footer-inner {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 48px;
  padding: 60px 20px 40px;
}

.footer-logo {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 16px;
}

.footer-logo span:first-child {
  font-size: 1.8rem;
}

.footer-logo-name {
  font-family: var(--font-heading);
  font-size: 1.5rem;
  color: var(--pink-soft);
  font-weight: 700;
}

.footer-bio {
  font-size: 0.9rem;
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.6);
  margin-bottom: 20px;
}

.footer-socials {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.social-link {
  padding: 8px 16px;
  border-radius: 40px;
  font-size: 0.85rem;
  font-weight: 600;
  transition: var(--transition);
}

.instagram {
  background: rgba(233, 30, 123, 0.15);
  color: var(--pink-soft);
  border: 1px solid rgba(233, 30, 123, 0.3);
}

.instagram:hover {
  background: var(--pink-primary);
  color: white;
}

.whatsapp {
  background: rgba(37, 211, 102, 0.15);
  color: #7ffbb3;
  border: 1px solid rgba(37, 211, 102, 0.3);
}

.whatsapp:hover {
  background: #25d366;
  color: white;
}

.footer-links h4,
.footer-contact h4 {
  font-family: var(--font-heading);
  font-size: 1rem;
  color: var(--pink-soft);
  margin-bottom: 18px;
}

.footer-links ul,
.footer-contact ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.footer-links li a,
.footer-contact li a {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.6);
  transition: color 0.2s;
}

.footer-links li a:hover,
.footer-contact li a:hover {
  color: var(--pink-soft);
}

.footer-contact li:not(:has(a)) {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.5);
}

.footer-bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding: 20px;
  text-align: center;
}

.footer-bottom p {
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.4);
}

@media (max-width: 768px) {
  .footer-inner {
    grid-template-columns: 1fr;
    gap: 32px;
    padding: 40px 20px 32px;
  }
}
</style>
