function toggle(){
    var x = document.getElementById("form1");
    var y = document.getElementById("form2");
    var z = document.getElementById("form3");
    x.style.display = "none";
    y.style.display = "block";
    z.style.display = "none";
    
}
function toggle1(){
    var x = document.getElementById("form1");
    var y = document.getElementById("form2");
    var z = document.getElementById("form3");
    x.style.display = "none";

    y.style.display = "none";
    z.style.display = "block";
    
}
function back(){
    var x = document.getElementById("form1");
    var y = document.getElementById("form2");
    var z = document.getElementById("form3");
    x.style.display = "block";
    y.style.display = "none";
    z.style.display = "none";
    
}
function back1(){
    var x = document.getElementById("form1");
    var y = document.getElementById("form2");
    var z = document.getElementById("form3");
    x.style.display = "none";

    y.style.display = "block";
    z.style.display = "none";
    
}

const image_input = document.querySelector("#infile"); 
var uploaded_image = ""; 

image_input.addEventListener("change", function(){
   
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        uploaded_image = reader.result;
        document.querySelector("#Imagepreview").style.background = 'url(${uploaded_image))'                    
    });
    reader.readAsDataURL(this.files[0]);
})