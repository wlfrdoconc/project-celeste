//Targeting the navbar__menu class in index.html
const menuLinks = document.querySelector('navbar__menu')

menu.addEventListener('click', function() {
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
})


//Unfinished 
function goToAbout() {
    location.href = 'about.html'; // Redirects to the about page
  }
