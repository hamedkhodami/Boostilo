    // var swipernews = new Swiper(".swiper", {
    //     loop: true,
    //   navigation: {
    //     nextEl: ".swiper-button-prev-custom",
    //     prevEl: ".swiper-button-next-custom",
    //   },
    // });


    const swiper2 = new Swiper("#jjj", {
        direction: 'horizontal',
        autoplay: {
          delay: 2000,
          loop:true,
        },
        slidesPerView: 2,
        spaceBetween: 10,
        navigation: {
        nextEl: ".swiper-button-prev-custom",
        prevEl: ".swiper-button-next-custom",
      },
      loop: true,
      navigation: {
        nextEl: ".swiper-button-prev-custom",
        prevEl: ".swiper-button-next-custom",
      }
    });

    const swiperblog = new Swiper(".blog", {
      direction: 'horizontal',
      autoplay: {
        delay: 2000,
        loop:true,
      },
      breakpoints: {
        340: {
          slidesPerView:1,

        },
          600: {
            slidesPerView:1,
            spaceBetween: 10, // <- doesn't work
          },
          700: {
            slidesPerView:2,
            spaceBetween: 10, // <- doesn't work
          },
          992: {
            slidesPerView:2,
            spaceBetween: 10, // <- doesn't work
          },
          1200: {
              slidesPerView: 2,
              spaceBetween: 10, // <- doesn't work

            },
        },

  });

  const swipercommentuser = new Swiper("#user-comment", {
    direction: 'horizontal',
    autoplay: {
      delay: 2000,
      loop:true,
    },
    breakpoints: {
      340: {
        slidesPerView:2,
        spaceBetween: 10, 
        
      },
        600: {
          slidesPerView:2,
          spaceBetween: 10, // <- doesn't work
        },
        700: {
          slidesPerView:2,
          spaceBetween: 10, // <- doesn't work
        },
        992: {
          slidesPerView:2,
          spaceBetween: 10, // <- doesn't work
        },
        1200: {
            slidesPerView: 2,
            spaceBetween: 10, // <- doesn't work
  
          },
      },
   
});