// Dynamic changes for year
document.getElementById("year").textContent = new Date().getFullYear();

// Dynamic changes for the title
const links = document.querySelectorAll("nav a");

links.forEach((link) => {
  link.addEventListener("click", (e) => {
    e.preventDefault();

    const newTitle = link.textContent;
    document.title = "Mooserage | " + newTitle;
  });
});
