
const submenu_open_btn = document.querySelector(".submenu-open-btn")
const submenu = document.querySelector(".submenu")
const navOpenBtn = document.querySelector(".nav-icon")
const navCloseBtn = document.querySelector(".nav-close-btn")
const nav = document.querySelector(".nav")
const overlay = document.querySelector(".overlay")

// -------show/hide submenu in mobile----------//
submenu_open_btn.addEventListener("click", (e) => {
    e.currentTarget.parentElement.classList.toggle("text-purple-600")
    submenu.classList.toggle("submenu--open")
})

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
// document.addEventListener('DOMContentLoaded', () => {
//     const buttons = document.querySelectorAll('.btn');
//     const contents = document.querySelectorAll('.content');
//     buttons.forEach(button => {
//         button.addEventListener('click', () => {
//             const contentId = button.getAttribute('data-content');
//             const content = document.getElementById(contentId);
           
//             if (window.innerWidth > 768) {
//                 buttons.forEach(btn => btn.classList.remove('active'));
//                 contents.forEach(content => {
//                     content.classList.remove('active');
//                     content.style.display = 'none';
//                 });

//                 button.classList.add('active');
//                 content.classList.add('active');
//                 content.style.display = 'block';
//             } else {
//                 buttons.forEach(btn => {
//                     btn.classList.remove('active');
//                     // document.getElementById(btn.getAttribute('data-content')).style.display = 'none';
//                 });
//                 contents.forEach(item => {
//                     item.style.display = "none";
//                 })

//                 button.classList.toggle('active');
//                 content.style.display = 'block';
//                 button.insertAdjacentElement('afterend', content);

//             }
//         });
//     });
// });

// // تنظیم محتوای اولیه برای عرض‌ کمتر از 768 پیکسل
// window.addEventListener('DOMContentLoaded', () => {
//     if (window.innerWidth <= 768) {
//         const contentId = 'content1';
//         const activeButton = document.querySelector(`.btn[data-content="${'content1'}"]`);
//         const content = document.getElementById(contentId);

//         // activeButton.classList.add('active');
//         content.style.display = 'block';

//         // اضافه کردن محتوای content1 به زیر دکمه اول
//         activeButton.insertAdjacentElement('afterend', content);
//     }
// });


document.addEventListener('DOMContentLoaded', () => {
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
                buttons.forEach(btn => btn.classList.remove('active'));
                contents.forEach(item => item.style.display = 'none');

                button.classList.toggle('active');
                content.style.display = 'block';
                button.insertAdjacentElement('afterend', content);
            }
        });
    });

    window.addEventListener('resize', () => {
        location.reload();
    });
});

// تنظیم محتوای اولیه برای عرض‌ کمتر از 768 پیکسل
window.addEventListener('DOMContentLoaded', () => {
    if (window.innerWidth <= 768) {
        const contentId = 'content1';
        const activeButton = document.querySelector(`.btn[data-content="${contentId}"]`);
        const content = document.getElementById(contentId);

        content.style.display = 'block';
        activeButton.insertAdjacentElement('afterend', content);
    }
});
