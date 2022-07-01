function toggle(){
    var x = document.getElementById("form1");
    var y = document.getElementById("form2");
    x.style.display = "none";
    y.style.display = "block";
    
}
function toggle1(){
    var x = document.getElementById("form1");
    var y = document.getElementById("form2");
    x.style.display = "block";
    
    
    y.style.display = "none";
    
}

var input = document.getElementById("input-file");
var prev = document.getElementById("preview");

input.addEventListener("change", function(event){
    if(event.target.files.length == 0){
        return;
    }
    var tempUrl = URL.createObjectURL(event.target.files[0]);
    prev.setAttribute("src", tempUrl);
});
