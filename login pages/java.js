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

let login = document.querySelector(".loginbutton")
login.addEventListener("click",()=>{
    if(pass.value==="1234"){
        console.log("login")
        login.disabled=true;
        window.location.href = "College-project\index.html";
    }else{
        alert("try again");
    }
})