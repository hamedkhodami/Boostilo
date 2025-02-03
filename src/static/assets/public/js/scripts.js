const submenu_open_btn = document.querySelectorAll(".submenu-open-btn");
const submenu = document.querySelectorAll(".submenu");
const openIcons = document.querySelectorAll(".open-icon");
const closeIcons = document.querySelectorAll(".close-icon");

if (window.innerWidth <= 768) {
    submenu_open_btn.forEach((item, index) => {
        item.addEventListener("click", () => {
            const submenuEl = submenu[index];
            submenuEl.classList.toggle("submenu--open");
        });
    });
}

const submenu_open_btns = document.querySelectorAll(".submenu-open-btn");
const submenus = document.querySelectorAll(".submenu");

if (window.innerWidth > 768) {
    submenu_open_btns.forEach((item, index) => {
        const submenu = submenus[index];
        const openIcon = openIcons[index];
        const closeIcon = closeIcons[index];

        item.addEventListener("mouseenter", () => {
            submenu.classList.add("submenu--open");  
            openIcon.classList.add("hidden");
            closeIcon.classList.remove("hidden");
        });

        
        submenu.addEventListener("mouseenter", () => {
            submenu.classList.add("submenu--open"); 
           
        });

        submenu.addEventListener("mouseleave", () => {
            submenu.classList.remove("submenu--open"); 
            openIcon.classList.remove("hidden");
            closeIcon.classList.add("hidden");
        });
    });
}




const navOpenBtn = document.querySelector(".nav-icon")
const navCloseBtn = document.querySelector(".nav-close-btn")
const nav = document.querySelector(".nav")
const overlay = document.querySelector(".overlay")

//---------show/hide menu bar in mobile--------------//
navOpenBtn.addEventListener("click", () => {
    nav.classList.remove("-left-64")
    nav.classList.add("left-0")
    // ----------handle with class --------------//
    overlay.classList.add("overlay--visible")
})

function closeNav() {
    nav.classList.remove("left-0")
    nav.classList.add("-left-64")
    // ----------handle with class --------------//
    overlay.classList.remove("overlay--visible")
}
const closeNavAndOverlay = () => {
    nav.classList.remove("left-0");
    nav.classList.add("-left-64");
    overlay.classList.remove("overlay--visible");
};
navCloseBtn.addEventListener("click", closeNavAndOverlay);
overlay.addEventListener("click", closeNavAndOverlay);






    // js for services boostiloo//

    const buttons = document.querySelectorAll('.btn');
    const contents = document.querySelectorAll('.content');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const contentId = button.getAttribute('data-content');
            const content = document.getElementById(contentId);

            if (window.innerWidth > 768) {
                buttons.forEach(btn => btn.classList.remove('active'));
                contents.forEach(content => {
                    content.classList.remove('active');
                    content.style.display = 'none';
                });

                button.classList.add('active');
                content.classList.add('active');
                content.style.display = 'block';
            } else {
                buttons.forEach(btn => {
                    btn.classList.remove('active');
                });
                contents.forEach(item => {
                    item.style.display = "none";
                })

                button.classList.toggle('active');
                content.style.display = 'block';
                button.parentNode.insertBefore(content, button.nextSibling);
            }
        });
    });

    // تنظیم محتوای اولیه برای عرض‌ کمتر از ۷۶۸ پیکسل

    if (window.innerWidth <= 768) {
        // پیدا کردن دکمه فعال و محتوای مربوطه
        const activeButton = document.querySelector('.btn.active');
        const activeContentId = activeButton ? activeButton.getAttribute('data-content') : 'content1'; // اگر دکمه‌ای فعال نبود، از content1 استفاده کن
        const activeContent = document.getElementById(activeContentId);

        // مخفی کردن همه محتواها
        document.querySelectorAll('.content').forEach(content => {
            content.style.display = 'none';
        });

        // نمایش محتوای فعال
        if (activeContent) {
            activeContent.style.display = 'block';
            activeButton.parentNode.insertBefore(activeContent, activeButton.nextSibling);
        }
    }

//document.addEventListener('DOMContentLoaded', () => {
//    const buttons = document.querySelectorAll('.btn');
//    const contents = document.querySelectorAll('.content');
//
//    buttons.forEach(button => {
//        button.addEventListener('click', () => {
//            const contentId = button.getAttribute('data-content');
//            const content = document.getElementById(contentId);
//
//            if (window.innerWidth > 768) {
//                buttons.forEach(btn => btn.classList.remove('active'));
//                contents.forEach(content => {
//                    content.classList.remove('active');
//                    content.style.display = 'none';
//                });
//
//                button.classList.add('active');
//                content.classList.add('active');
//                content.style.display = 'block';
//            } else {
//                buttons.forEach(btn => btn.classList.remove('active'));
//                contents.forEach(item => item.style.display = 'none');
//
//                button.classList.toggle('active');
//                content.style.display = 'block';
//                button.insertAdjacentElement('afterend', content);
//            }
//        });
//    });
//
//    window.addEventListener('resize', () => {
//        location.reload();
//    });
//});
//

//window.addEventListener('DOMContentLoaded', () => {
//    if (window.innerWidth <= 768) {
//        const contentId = 'content1';
//        const activeButton = document.querySelector(`.btn[data-content="${contentId}"]`);
//        const content = document.getElementById(contentId);
//
//        content.style.display = 'block';
//        activeButton.insertAdjacentElement('afterend', content);
//    }
//});






// popup video//
const openPopupButtons = document.querySelectorAll('.openPopup');
const closePopupButtons = document.querySelectorAll('.closePopup');

openPopupButtons.forEach(button => {
  button.addEventListener("click", () => {
    const popupId = button.getAttribute("data-popup-target");
    document.getElementById(popupId).classList.remove("hidden");
  });
});

closePopupButtons.forEach(button => {
  button.addEventListener("click", () => {
    const popup = button.closest('.popup');
    if (popup) {
      const video = popup.querySelector('video');
        if (video) {
          video.pause();
          video.currentTime = 0;
        }
      popup.classList.add("hidden");
    }
  });
});

// end popup video//