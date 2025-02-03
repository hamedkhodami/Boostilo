     var swipernews = new Swiper(".news", {
         loop: true,
       navigation: {
         nextEl: ".swiper-button-prev-custom",
         prevEl: ".swiper-button-next-custom",
       },
     });



     const swiper2 = new Swiper("#jjj", {
      direction: 'horizontal',
      autoplay: {
        delay: 3000,
        disableOnInteraction: false, // برای اینکه چرخش بعد از تعامل کاربر همچنان ادامه پیدا کند
        loop: true,
      },
      breakpoints: {
        340: {
          slidesPerView: 1,
        },
        600: {
          slidesPerView: 2,
          spaceBetween: 10,
        },
        700: {
          slidesPerView: 2,
          spaceBetween: 10,
        },
        992: {
          slidesPerView: 2,
          spaceBetween: 10,
        },
        1200: {
          slidesPerView: 2,
          spaceBetween: 10,
        },
      },
      navigation: {
        nextEl: ".swiper-button-prev-custom",
        prevEl: ".swiper-button-next-custom",
      },
      on: {
        init: function () {
          this.slides.forEach((slide) => {
            slide.addEventListener('mouseenter', () => {
              this.autoplay.stop();
            });
            slide.addEventListener('mouseleave', () => {
              this.autoplay.start();
            });
            slide.addEventListener('touchstart', () => { // برای توقف چرخش در دستگاه های لمسی
              this.autoplay.stop();
            });
            slide.addEventListener('touchend', () => { // برای ادامه چرخش در دستگاه های لمسی
              this.autoplay.start();
            });
          });
        },
      },
     });



     const swiperblog = new Swiper(".blog", {
      direction: 'horizontal',
      autoplay: {
        delay: 3000,
        disableOnInteraction: false, 
        loop: true,
      },
      breakpoints: {
        340: {
          slidesPerView: 1,
        },
        600: {
          slidesPerView: 1,
          spaceBetween: 10,
        },
        700: {
          slidesPerView: 2,
          spaceBetween: 10,
        },
        992: {
          slidesPerView: 2,
          spaceBetween: 10,
        },
        1200: {
          slidesPerView: 2,
          spaceBetween: 10,
        },
      },
      navigation: {
        nextEl: ".swiper-button-prev-custom",
        prevEl: ".swiper-button-next-custom",
      },
      on: {
        init: function () {
          this.slides.forEach((slide) => {
            slide.addEventListener('mouseenter', () => {
              this.autoplay.stop();
            });
            slide.addEventListener('mouseleave', () => {
              this.autoplay.start();
            });
            slide.addEventListener('touchstart', () => { 
              this.autoplay.stop();
            });
            slide.addEventListener('touchend', () => { 
              this.autoplay.start();
            });
          });
        },
      },
    });


  

