const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('.main-nav');

function closeMenu() {
  menuButton?.classList.remove('active');
  navigation?.classList.remove('open');
  menuButton?.setAttribute('aria-expanded', 'false');
  document.body.classList.remove('menu-open');
}

menuButton?.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.classList.toggle('active', open);
  navigation.classList.toggle('open', open);
  menuButton.setAttribute('aria-expanded', String(open));
  document.body.classList.toggle('menu-open', open);
});

navigation?.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));
window.addEventListener('resize', () => { if (window.innerWidth > 850) closeMenu(); });
document.querySelectorAll('#year').forEach((year) => { year.textContent = new Date().getFullYear(); });

const quoteForm = document.getElementById('quote-form');
const requestedService = new URLSearchParams(window.location.search).get('service');
const serviceMap = { remote: 'Remote IT Troubleshooting', 'smart-hands': 'Network and Data Center Smart Hands', documentation: 'Technical SOP and Runbook Creation' };

if (quoteForm && requestedService) quoteForm.elements.service.value = serviceMap[requestedService] || requestedService;

quoteForm?.addEventListener('submit', (event) => {
  event.preventDefault();
  const data = new FormData(quoteForm);
  const subject = encodeURIComponent(`Quote request: ${data.get('service')}`);
  const body = encodeURIComponent(`Name: ${data.get('name')}\nCompany: ${data.get('company') || 'Not provided'}\nEmail: ${data.get('email')}\nPhone: ${data.get('phone') || 'Not provided'}\nService: ${data.get('service')}\nLocation: ${data.get('location')}\nPreferred date: ${data.get('date') || 'Flexible'}\n\nScope of work:\n${data.get('message')}`);
  window.location.href = `mailto:REPLACE-WITH-BUSINESS-EMAIL?subject=${subject}&body=${body}`;
});
