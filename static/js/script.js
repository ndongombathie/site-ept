/* jquery */

let inscriptionbutton=$("#inscription");
let connexionbutton=$("#connexion");
let modal = $("#modal");
let loginconnexion = $(".login-connexion");
let section = $(".section");

console.log(inscription);

inscriptionbutton.click(() =>{
    modal.css({"display":"block"});
    loginconnexion.css({"display":"none"});
    section.css({"filter":"blur(2px)"});

})

connexionbutton.click(() =>{
    loginconnexion.css({"display":"block"});
    modal.css({"display":"none"});
    section.css({"filter":"blur(2px)"});
})
        
