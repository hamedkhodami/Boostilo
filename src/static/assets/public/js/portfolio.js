document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.btn-portfolio');
    const samples = document.querySelectorAll('.sample');

    
    const allButton = document.querySelector('[data-category="all"]');
    allButton.classList.add('active'); // دکمه "all" فعال است
    samples.forEach(sample => sample.classList.remove('hidden')); 

    
    buttons.forEach(button => {
        button.addEventListener('click', function() {

            buttons.forEach(btn => btn.classList.remove('active'));

            button.classList.add('active');

            const category = button.getAttribute('data-category');

            samples.forEach(sample => {
                if (category === 'all' || sample.getAttribute('data-category') === category) {
                    sample.classList.remove('hidden');
                } else {
                    sample.classList.add('hidden');
                }
            });
        });
    });
});
