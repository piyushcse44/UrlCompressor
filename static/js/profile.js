var menu_btn = document.querySelector("#menu-btn");
var menu_btnx = document.querySelector(".menu-btnx");
var sidebar = document.querySelector("#sidebar");
var container = document.querySelector(".my-container");
var containerx = document.querySelector(".my-containerx");
menu_btn.addEventListener("click", () => {
  sidebar.classList.toggle("active-nav");
  container.classList.toggle("active-cont");
});
menu_btnx.addEventListener("click", () => {
  sidebar.classList.toggle("active-nav");
  containerx.classList.toggle("active-cont");
});

const togglePassword = document.querySelector("#togglePassword");
const togglePassword2 = document.querySelector("#togglePassword2");
console.log(togglePassword2);
const password = document.querySelector("#password");
const password2 = document.querySelector("#password2");
console.log(password2, 2);
togglePassword.addEventListener("click", () => {
  const type =
    password.getAttribute("type") === "password" ? "text" : "password";
  password.setAttribute("type", type);
  togglePassword.classList.toggle("bi-eye");
});
togglePassword2.addEventListener("click", () => {
  const type =
    password2.getAttribute("type") === "password" ? "text" : "password";
  password2.setAttribute("type", type);
  togglePassword2.classList.toggle("bi-eye");
});

document.addEventListener("DOMContentLoaded", function () {
  // Get the elements
  var profileLink = document.querySelector("#HitProfile");
  var linkLink = document.querySelector("#HitLink");
  var profileContainer = document.querySelector("#Profile");
  var linkContainer = document.querySelector("#Link-s");

  // Add click event listeners
  profileLink.addEventListener("click", function () {
    console.log("from Profile");
    profileContainer.classList.remove("displayNone");
    linkContainer.classList.add("displayNone");
  });

  linkLink.addEventListener("click", function () {
    console.log("from Link");
    linkContainer.classList.remove("displayNone");
    profileContainer.classList.add("displayNone");
  });
});
