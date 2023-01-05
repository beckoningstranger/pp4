var menu_btn = document.querySelector("#toggle-sidebar-btn")
var sidebar = document.querySelector("#sidebar")
var container = document.querySelector(".sidebar-button-container")
menu_btn.addEventListener("click", () => {
    sidebar.classList.toggle("active-nav")
    container.classList.toggle("active-cont")
})
