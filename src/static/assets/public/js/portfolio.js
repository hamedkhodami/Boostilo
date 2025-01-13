document.addEventListener("DOMContentLoaded", () => {
    const buttonPortfolio = document.querySelectorAll(".btn-portfolio");
    const samples = document.querySelectorAll(".sample");

    if (buttonPortfolio.length > 0) {
        const defaultButton = buttonPortfolio[0];
        const defaultCategory = defaultButton.getAttribute("data-category");

        defaultButton.classList.add("active");

        samples.forEach(sample => {
            if (sample.getAttribute("data-category") === defaultCategory) {
                sample.classList.remove("hidden");
            }
        });
    }

    buttonPortfolio.forEach((button) => {
        button.addEventListener("click", () => {
            buttonPortfolio.forEach((btn) => btn.classList.remove("active"));

            button.classList.add("active");

            const category = button.getAttribute("data-category");
            samples.forEach((sample) => {
                sample.classList.add("hidden");
                if (sample.getAttribute("data-category") === category) {
                    sample.classList.remove("hidden");
                }
            });
        });
    });
});