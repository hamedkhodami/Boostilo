
// active category btn
const btns = document.querySelectorAll(".btn-category");
btns[0].classList.add('active');
console.log(btns[0])
btns.forEach((button) => {
    button.addEventListener("click", () => {
        btns.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
    });
});


document.addEventListener('DOMContentLoaded', () => {
    const categoryButtons = document.querySelectorAll('.btn-category');

    // انتخاب دکمه اول و فعال کردن آن
    const firstButton = categoryButtons[0];
    firstButton.classList.add('active');

    // نمایش تصاویر مربوط به دسته اول
    const firstCategoryId = firstButton.getAttribute('category-id');
    displayImages(firstCategoryId);

    categoryButtons.forEach(button => {
        button.addEventListener('click', () => {
            // حذف کلاس‌های فعال از تمامی دکمه‌ها
            categoryButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            const categoryId = button.getAttribute('category-id');
            displayImages(categoryId);
        });
    });

    function displayImages(categoryId) {
        const gridItems = document.querySelectorAll(".grid-item");
        const gridContainer = document.querySelector('.grid-container');

        // ابتدا تمام تصاویر را مخفی می‌کنیم
        gridItems.forEach(image => image.classList.add('hidden'));

        // فقط تصاویری که مربوط به دسته انتخابی هستند را نشان می‌دهیم
        gridItems.forEach((item) => {
            if (item.getAttribute("category-img-id") === categoryId) {
                item.classList.remove('hidden');
            }
        });
    }
});








