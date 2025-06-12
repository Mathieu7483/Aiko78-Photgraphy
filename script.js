document.addEventListener("contextmenu", (event) => event.preventDefault());
document.addEventListener("dragstart", (event) => {
  event.preventDefault();
});

const burgerMenu = document.querySelector(".burger-menu");
const navLinks = document.querySelector(".nav-links");

burgerMenu.addEventListener("click", () => {
  navLinks.classList.toggle("active");
  burgerMenu.classList.toggle("active");
});

const galleryImages = document.querySelectorAll(".gallery a");
const lightbox = document.getElementById("lightbox");
const lightboxImage = document.getElementById("lightbox-image");
const lightboxClose = document.querySelector(".lightbox-close");
const lightboxReturnButton = document.getElementById("lightbox-return");

galleryImages.forEach((imageLink) => {
  imageLink.addEventListener("click", function (event) {
    event.preventDefault();
    const imageSrc = this.getAttribute("data-lightbox-image");
    const imageAlt = this.getAttribute("data-alt") || "";
    lightboxImage.src = imageSrc;
    lightboxImage.alt = imageAlt;
    lightbox.style.display = "block";
  });
});

lightboxClose.addEventListener("click", function () {
  lightbox.style.display = "none";
  lightboxImage.src = "";
  lightboxImage.alt = "";
});

lightbox.addEventListener("click", function (event) {
  if (event.target === this) {
    lightbox.style.display = "none";
    lightboxImage.src = "";
    lightboxImage.alt = "";
  }
});

document.addEventListener("keydown", function (event) {
  if (event.key === "Escape") {
    lightbox.style.display = "none";
    lightboxImage.src = "";
    lightboxImage.alt = "";
  }
});

// Écouteur d'événement pour le bouton "Retour à la galerie"
lightboxReturnButton.addEventListener("click", function () {
  lightbox.style.display = "none";
  lightboxImage.src = "";
  lightboxImage.alt = "";
});
