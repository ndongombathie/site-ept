/* jquery */

let inscriptionbutton=$("#inscription");
let modal = $("#modal");
let section = $(".section");

console.log(inscription);

inscriptionbutton.click(() =>{
    modal.css({"display":"block"});
    section.css({"filter":"blur(2px)"});

})
