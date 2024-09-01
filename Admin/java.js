let login = document.querySelector(".logout")
login.addEventListener("click",()=>{
        window.location.href = "login.html";
})
window.onload = function() {
        const profilePic = document.getElementById('profilePic');
        const uploadPic = document.getElementById('uploadPic');
        
        uploadPic.addEventListener('change', function() {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    profilePic.src = e.target.result;
                }
                reader.readAsDataURL(file);
            }
        });
    };
    
