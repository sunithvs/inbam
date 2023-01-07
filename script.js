const body = document.body;

const header = document.querySelector(".header");
const toggleMenu = document.querySelector(".toggle-menu");

toggleMenu.addEventListener("click", openMenu);

function openMenu() {
  if (header.classList.contains("header--active")) {
    header.classList.remove("header--active");
    body.classList.remove("body--noscroll");
  } else {
    header.classList.add("header--active");
    body.classList.add("body--noscroll");
  }
}