$(document).ready(function(){
    document.getElementById("name1").addEventListener("keyup", e => {
        if (e.target.value == "") {
            document.getElementById("b1").disabled = true;
        }
        else {
            document.getElementById("b1").disabled = false;
        }
    })
});
    
function submit(){

    var n1  = document.getElementById("name1");
    var c1  = document.getElementById("textarea1");
    var p1  = document.getElementById("PCnum");

    if ( c1.value == "" || n1.value == "" || p1.value == ""  ){
        alert("please complete the fill up");
        
    } 
    else{
        document.getElementById("name1").value ='';
        document.getElementById("textarea1").value ='';
        document.getElementById("PCnum").value ='';
        document.getElementById("list1").value ='default';
        document.getElementById("list2").value ='default';

    }
    

}


function cancel1(){
    document.getElementById("name1").value ='';
    document.getElementById("textarea1").value ='';
    document.getElementById("PCnum").value ='';
    document.getElementById("list1").value ='default';
    document.getElementById("list2").value ='default';
        

}
function cancel2(){
    document.getElementById("name1").value ='';
    document.getElementById("textarea1").value ='';
    document.getElementById("PCnum").value ='';
    document.getElementById("list1").value ='default';
    document.getElementById("list2").value ='default';
        

}


