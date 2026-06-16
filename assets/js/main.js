/**
* Template Name: Arsha
* Template URL: https://bootstrapmade.com/arsha-free-bootstrap-html-template-corporate/
* Updated: Feb 22 2025 with Bootstrap v5.3.3
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

(function() {
  "use strict";

  // Cache core global element selections
  const bodyEl = document.querySelector('body');
  const headerEl = document.querySelector('#header');
  const scrollTopBtn = document.querySelector('.scroll-top');
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  /**
   * Throttle helper to protect scroll performance
   */
  function throttle(func, delay) {
    let timeout = null;
    return function(...args) {
      if (!timeout) {
        timeout = setTimeout(() => {
          func.apply(this, args);
          timeout = null;
        }, delay);
      }
    };
  }

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    if (!headerEl) return;
    const isStickyOrFixed = headerEl.classList.contains('scroll-up-sticky') || 
                            headerEl.classList.contains('sticky-top') || 
                            headerEl.classList.contains('fixed-top');
    if (!isStickyOrFixed) return;

    window.scrollY > 100 ? bodyEl.classList.add('scrolled') : bodyEl.classList.remove('scrolled');
  }

  document.addEventListener('scroll', throttle(toggleScrolled, 15));
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  function mobileNavToggle() {
    bodyEl.classList.toggle('mobile-nav-active');
    if (mobileNavToggleBtn) {
      mobileNavToggleBtn.classList.toggle('bi-list');
      mobileNavToggleBtn.classList.toggle('bi-x');
    }
  }

  if (mobileNavToggleBtn) {
    mobileNavToggleBtn.addEventListener('click', mobileNavToggle);
  }

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navLink => {
    navLink.addEventListener('click', () => {
      if (bodyEl.classList.contains('mobile-nav-active')) {
        mobileNavToggle();
      }
    });
  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(dropdownToggle => {
    dropdownToggle.addEventListener('click', function(e) {
      e.preventDefault();
      const parentLi = this.parentNode;
      const nextUl = parentLi.nextElementSibling;

      parentLi.classList.toggle('active');
      if (nextUl) {
        nextUl.classList.toggle('dropdown-active');
      }
      e.stopImmediatePropagation();
    });
  });

  /**
   * Preloader
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  /**
   * Scroll top button
   */
  function toggleScrollTop() {
    if (!scrollTopBtn) return;
    window.scrollY > 100 ? scrollTopBtn.classList.add('active') : scrollTopBtn.classList.remove('active');
  }

  if (scrollTopBtn) {
    scrollTopBtn.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  document.addEventListener('scroll', throttle(toggleScrollTop, 15));
  window.addEventListener('load', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    if (typeof AOS !== 'undefined') {
      AOS.init({
        duration: 600,
        easing: 'ease-in-out',
        once: true,
        mirror: false
      });
    }
  }
  window.addEventListener('load', aosInit);

  /**
   * Initiate glightbox
   */
  if (typeof GLightbox !== 'undefined') {
    GLightbox({ selector: '.glightbox' });
  }

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    if (typeof Swiper === 'undefined') return;
    
    document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {
      const configEl = swiperElement.querySelector(".swiper-config");
      if (!configEl) return;

      let config = JSON.parse(configEl.innerHTML.trim());

      if (swiperElement.classList.contains("swiper-tab")) {
        if (typeof initSwiperWithCustomPagination === 'function') {
          initSwiperWithCustomPagination(swiperElement, config);
        }
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }
  window.addEventListener("load", initSwiper);

  /**
   * Frequently Asked Questions Toggle
   */
  document.querySelectorAll('.faq-item h3, .faq-item .faq-toggle').forEach((faqItem) => {
    faqItem.addEventListener('click', () => {
      faqItem.parentNode.classList.toggle('faq-active');
    });
  });

  /**
   * Animate the skills items on reveal
   */
  const skillsAnimation = document.querySelectorAll('.skills-animation');
  if (skillsAnimation.length > 0 && typeof Waypoint !== 'undefined') {
    skillsAnimation.forEach((item) => {
      new Waypoint({
        element: item,
        offset: '80%',
        handler: function() {
          let progressBars = item.querySelectorAll('.progress .progress-bar');
          progressBars.forEach(el => {
            el.style.width = el.getAttribute('aria-valuenow') + '%';
          });
        }
      });
    });
  }

  /**
   * Init isotope layout and filters
   */
  document.querySelectorAll('.isotope-layout').forEach(function(isotopeItem) {
    if (typeof Isotope === 'undefined' || typeof imagesLoaded === 'undefined') return;

    let layout = isotopeItem.getAttribute('data-layout') ?? 'masonry';
    let filter = isotopeItem.getAttribute('data-default-filter') ?? '*';
    let sort = isotopeItem.getAttribute('data-sort') ?? 'original-order';
    let container = isotopeItem.querySelector('.isotope-container');
    
    if (!container) return;

    let initIsotope;
    imagesLoaded(container, function() {
      initIsotope = new Isotope(container, {
        itemSelector: '.isotope-item',
        layoutMode: layout,
        filter: filter,
        sortBy: sort
      });
    });

    isotopeItem.querySelectorAll('.isotope-filters li').forEach(function(filterBtn) {
      filterBtn.addEventListener('click', function() {
        const activeFilter = isotopeItem.querySelector('.isotope-filters .filter-active');
        if (activeFilter) activeFilter.classList.remove('filter-active');
        
        this.classList.add('filter-active');
        
        if (initIsotope) {
          initIsotope.arrange({
            filter: this.getAttribute('data-filter')
          });
        }
        
        aosInit();
      }, false);
    });
  });

  /**
   * Correct scrolling position upon page load for URLs containing hash links.
   */
  window.addEventListener('load', function() {
    if (window.location.hash) {
      let targetSection = document.querySelector(window.location.hash);
      if (targetSection) {
        setTimeout(() => {
          let scrollMarginTop = getComputedStyle(targetSection).scrollMarginTop;
          window.scrollTo({
            top: targetSection.offsetTop - (parseInt(scrollMarginTop) || 0),
            behavior: 'smooth'
          });
        }, 100);
      }
    }
  });

  /**
   * Navmenu Scrollspy
   */
  const navmenulinks = document.querySelectorAll('.navmenu a');

  function navmenuScrollspy() {
    const position = window.scrollY + 200;

    navmenulinks.forEach(navmenulink => {
      if (!navmenulink.hash) return;
      let section = document.querySelector(navmenulink.hash);
      if (!section) return;
      
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        document.querySelectorAll('.navmenu a.active').forEach(link => link.classList.remove('active'));
        navmenulink.classList.add('active');
      } else {
        navmenulink.classList.remove('active');
      }
    });
  }
  
  document.addEventListener('scroll', throttle(navmenuScrollspy, 30));
  window.addEventListener('load', navmenuScrollspy);

})();