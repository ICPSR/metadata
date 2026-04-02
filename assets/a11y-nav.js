document.addEventListener("DOMContentLoaded", function () {

  // Find sidebar navigation
  const menuItems = document.querySelectorAll(".wy-menu-vertical li");

  menuItems.forEach(item => {
    const link = item.querySelector("a");
    const submenu = item.querySelector("ul");

    if (link && submenu) {

      // Initial state
      link.setAttribute("aria-expanded", item.classList.contains("current") ? "true" : "false");

      link.addEventListener("click", function () {
        const expanded = link.getAttribute("aria-expanded") === "true";
        link.setAttribute("aria-expanded", expanded ? "false" : "true");
      });

    }
  });

});