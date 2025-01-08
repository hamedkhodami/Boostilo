
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


// Masonry gallery
document.addEventListener("DOMContentLoaded", function() {
    var elem = document.querySelector('.grid-container');
    
    var msnry = new Masonry(elem, {
        itemSelector: '.grid-item', 
        columnWidth: '.grid-item', 
        percentPosition: true, 
        gutter: 2, 
    });

    imagesLoaded(elem, function() {
        msnry.layout(); 
    });

    
});







