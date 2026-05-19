// SABBTCo. — small interactions

// Mobile nav toggle
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', () => {
      links.classList.toggle('open');
      toggle.textContent = links.classList.contains('open') ? '✕' : '☰';
    });
  }

  // Highlight active nav link
  const path = window.location.pathname.replace(/\/$/, '') || '/';
  document.querySelectorAll('.nav-links a[data-path]').forEach(a => {
    if (a.dataset.path === path) a.classList.add('active');
  });

  // Login tab switcher
  const tabs = document.querySelectorAll('.tab-switch button');
  const nameField = document.getElementById('register-name');
  tabs.forEach(btn => {
    btn.addEventListener('click', () => {
      tabs.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const mode = btn.dataset.mode;
      if (nameField) nameField.style.display = mode === 'register' ? 'flex' : 'none';
      const submit = document.getElementById('login-submit');
      if (submit) submit.textContent = mode === 'register' ? 'Create Account' : 'Sign In';
    });
  });

  // Quote form fake-submit (replace with Django POST handler)
  const quoteForm = document.getElementById('quote-form');
  const success = document.getElementById('quote-success');
  if (quoteForm) {
    quoteForm.addEventListener('submit', (e) => {
      e.preventDefault();
      quoteForm.style.display = 'none';
      if (success) success.style.display = 'block';
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Login form (replace with Django auth POST)
  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('Backend coming soon — connect Django auth here.');
    });
  }

  // Year in footer
  const y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
});
