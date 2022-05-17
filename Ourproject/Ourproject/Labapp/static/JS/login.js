



function validate ()
{
    var un = document.forms["log"]["uname"].value;
    var up = document.forms["log"]["upass"].value;
    
    if(un == "INSTRUCTOR@gmail.com" && up == "instructor")
    {
      window.location.href="{ url 'homepage' }";
    }
    else if(un == "UITCSTAFF@gmail.com" && up == "uitcstaff")
    {
        window.location.href="{% url 'register' %}";
    }

    else
    {
        alert("PLEASE INPUT THE RIGHT USERNAME AND PASSWORD")
    }

}

const show = () => {
    let password = document.getElementById("upass");
    let visibility = document.querySelector(".visibility");
    if (password.type === "password") {
      password.type = "text";
      visibility.style.color = "rgb(128, 0, 122)";
    } else {
      password.type = "password";
      visibility.style.color = "#fff";
    }
  };

function isEmpty(){
   let pass = document.getElementById("upass").value; 
   let name = document.getElementById("uname").value;
   
   
   
   if (name != "" && pass != ""  ){
       document.getElementById("log").removeAttribute("disabled");
       
   }
}
                     
                                