let pass = document.querySelector("#password");
let icon = document.querySelector(".icon");

icon.addEventListener("click", () => {
    if (pass.getAttribute("type") === "password") {
        pass.setAttribute("type", "text");
        icon.classList.add("fa-eye-slash")
        icon.classList.remove("fa-eye");
    } else {
        pass.setAttribute("type", "password");
        icon.classList.add("fa-eye");
        icon.classList.remove("fa-eye-slash")
    }
});