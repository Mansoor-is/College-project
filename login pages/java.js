let pass = document.querySelector("#password");
let icon = document.querySelector(".icon");

icon.addEventListener("click", () => {
    if (pass.getAttribute("type") === "password") {
        pass.setAttribute("type", "text");
    } else {
        pass.setAttribute("type", "password");
    }
});
// log in