/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./public/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily:{
        "INTER" : "INTER",
        "INTER regular" : "INTER Regular",
        "INTER Bold" : "INTER Bold",
      },

      container:{
        "center":true,
         padding:{
          DEFULT:"1rem",
          lg:"0.625rem"
         }
      },

      backgroundImage:{
        "home-desktop":"url(../images/boostiloaboutback.webp)",
        "boostilo-portfolio":"url(../images/portfolio.webp)",
        "backcomment":"url(../images/teambackground.webp)",
        "backservices":"url(../images/servicesbackground.webp)",
        'custom-back-services': 'url(../images/servicesback.webp)',
        "backcontact":"url(../images/custumback2.png)"
      },
    },
    screens:{
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1150px',
    },
    keyframes:{ 
      fadeIn: { 
        '0%': { opacity: 0 },
       '100%': { opacity: 1 },
       },
       },
      animation: {
         fadeIn: 'fadeIn 1s ease-in-out forwards',
       },
  },
  variants: {},
  plugins: [
    require('tailwind-clip-path'),
  ],
}

