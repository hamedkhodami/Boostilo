document.addEventListener("DOMContentLoaded" ,() =>{
    const buttonPortfolio = document.querySelectorAll(".btn-portfolio");
    const samples = document.querySelectorAll(".sample");


     buttonPortfolio[0].classList.add("active");
     samples.forEach(sample => {
     if (sample.getAttribute("data-category") === "category1") {
      sample.classList.remove("hidden"); }
      });



    buttonPortfolio.forEach((button) =>{
        button.addEventListener("click" , ()=>{

            buttonPortfolio.forEach((btn) =>{
                btn.classList.remove("active")
            })

             button.classList.add("active")
             const category = button.getAttribute("data-portfolio")

               // مخفی کردن همه نمونه‌کارها
            samples.forEach((sample) => sample.classList.add("hidden"));
            samples.forEach((sample) =>{
                if(sample.getAttribute("data-category") == category ){
                    sample.classList.remove("hidden")
                }
            })

        })
    })
})