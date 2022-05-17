function register(){

    var f1  = document.getElementById("Fullname");
    var p1  = document.getElementById("password");
    var em1  = document.getElementById("em");
    var n1  = document.getElementById("num1");
    var c1  = document.getElementById("com");
    var s1  = document.getElementById("staf");

    if ( f1.value == "" || n1.value == "" || p1.value == "" || em1.value == "" || s1.checked == false && c1.checked == false){
        alert("please complete the fill up");
        
    } 
    else{
        window.location="{% url 'homepage' %}";
        document.getElementById("Fullname").value ='';
        document.getElementById("password").value ='';
        document.getElementById("em").value ='';
        document.getElementById("com").checked ='';
        document.getElementById("staf").checked ='';
    }
    

}