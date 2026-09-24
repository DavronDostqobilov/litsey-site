document.addEventListener('DOMContentLoaded', function () {
  // Hero Carousel Slider
  const slides = document.querySelectorAll('.hero-slide');
  const prevBtn = document.querySelector('.slider-btn.prev');
  const nextBtn = document.querySelector('.slider-btn.next');
  let currentSlide = 0;

  function showSlide(index) {
    if (!slides.length) return;
    slides.forEach(slide => slide.classList.remove('active'));
    currentSlide = (index + slides.length) % slides.length;
    slides[currentSlide].classList.add('active');
  }

  if (prevBtn && nextBtn) {
    prevBtn.addEventListener('click', () => showSlide(currentSlide - 1));
    nextBtn.addEventListener('click', () => showSlide(currentSlide + 1));

    // Auto rotate every 6 seconds
    setInterval(() => {
      showSlide(currentSlide + 1);
    }, 6000);
  }

  // Mobile Menu Toggle
  const mobileToggle = document.querySelector('.mobile-toggle');
  const navMenu = document.querySelector('.nav-menu');

  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', function () {
      if (navMenu.style.display === 'flex') {
        navMenu.style.display = 'none';
      } else {
        navMenu.style.display = 'flex';
        navMenu.style.flexDirection = 'column';
        navMenu.style.position = 'absolute';
        navMenu.style.top = '100%';
        navMenu.style.left = '0';
        navMenu.style.right = '0';
        navMenu.style.background = '#ffffff';
        navMenu.style.padding = '20px';
        navMenu.style.boxShadow = '0 10px 25px rgba(0,0,0,0.1)';
      }
    });
  }

  // Counter animation for statistics
  const statNumbers = document.querySelectorAll('.stat-number');
  let animated = false;

  function animateStats() {
    if (animated || !statNumbers.length) return;
    statNumbers.forEach(stat => {
      const target = parseInt(stat.getAttribute('data-target') || '0', 10);
      let count = 0;
      const speed = Math.ceil(target / 40);
      const timer = setInterval(() => {
        count += speed;
        if (count >= target) {
          stat.textContent = target + '+';
          clearInterval(timer);
        } else {
          stat.textContent = count + '+';
        }
      }, 30);
    });
    animated = true;
  }

  window.addEventListener('scroll', function () {
    const statsRibbon = document.querySelector('.stats-ribbon');
    if (statsRibbon) {
      const rect = statsRibbon.getBoundingClientRect();
      if (rect.top <= window.innerHeight && rect.bottom >= 0) {
        animateStats();
      }
    }
  });

  // Initial trigger check if visible on page load
  animateStats();
});
