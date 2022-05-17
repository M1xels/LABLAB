$(document).ready(function(){
    b1.setAttribute("disabled","disabled");
    $("#b1").click(function(){
        b1.setAttribute("disabled","disabled");
        b2.removeAttribute("disabled");
        b3.removeAttribute("disabled");
        b4.removeAttribute("disabled");
        $("#fdata1").show();
        $("#fdata2").hide();
        $("#fdata3").hide();
        $("#fdata4").hide();
        
    });
    $("#b2").click(function(){
        b2.setAttribute("disabled","disabled");
        b3.removeAttribute("disabled");
        b4.removeAttribute("disabled");
        b1.removeAttribute("disabled");
        $("#fdata1").hide();
        $("#fdata2").show();
        $("#fdata3").hide();
        $("#fdata4").hide();
       
    });
    $("#b3").click(function(){
        b3.setAttribute("disabled","disabled");
        b1.removeAttribute("disabled");
        b2.removeAttribute("disabled");
        b4.removeAttribute("disabled");
        $("#fdata1").hide();
        $("#fdata2").hide();
        $("#fdata3").show();
        $("#fdata4").hide();
        
    });
    $("#b4").click(function(){
        b4.setAttribute("disabled","disabled");
        b1.removeAttribute("disabled");
        b2.removeAttribute("disabled");
        b3.removeAttribute("disabled");
        $("#fdata1").hide();
        $("#fdata2").hide();
        $("#fdata3").hide();
        $("#fdata4").show();
        
    });
});


document.getElementById("b1").disabled = true;

/*YES1 button*////////////////



    
    






function yes1(){
    
    var fname11 = document.getElementById("t11");
    var ddate12 = document.getElementById("t12");
    var timeIN13 = document.getElementById("t13");
    if (fname11.value == "" || ddate12.value == ""  || timeIN13.value == "" ){
        alert("please complete the fill up");
        
    }
        
    else{
        console.log("hahahahah");
        let O1 = "Laboratory 1 \n is Occupied by Class \n ";
        let V1 =  document.getElementById("t11") .value;

        var A1 = O1 + V1;


        document.getElementById("b1").innerText = A1;
        document.getElementById("s11").removeAttribute("disabled");
        document.getElementById("t14").removeAttribute("disabled");
        document.getElementById("to1").style.opacity = 1;

        document.getElementById("s12").setAttribute("disabled","disabled");
        document.getElementById("s13").setAttribute("disabled","disabled");
        modalob2.style.display = "block";
        
    }

    
    
    

    
}
/*document.getElementById("b2").innerHTML = '<img class="pic" src="desktop-computer.png" alt="image" ><br><h6 class="f">Lab1</h6>;*/
function yes2(){


    var fname21 = document.getElementById("t21");
    var ddate22 = document.getElementById("t22");
    var timeIN23 = document.getElementById("t23");
    if (fname21.value == "" || ddate22.value == ""  || timeIN23.value == "" ){
        alert("please complete the fill up");
        
    }
        
    else{
        console.log("hahahahah");
        let O2 = "Laboratory 2 \n is Occupied by Class \n ";
        let V2 =  document.getElementById("t21") .value;

        var A2 = O2 + V2;


        document.getElementById("b2").innerText = A2;
        document.getElementById("s21").removeAttribute("disabled");
        document.getElementById("t24").removeAttribute("disabled");
        document.getElementById("to2").style.opacity = 1;

        document.getElementById("s22").setAttribute("disabled","disabled");
        document.getElementById("s23").setAttribute("disabled","disabled");
    }
    

    
}
function yes3(){
    var fname31 = document.getElementById("t31");
    var ddate32 = document.getElementById("t32");
    var timeIN33 = document.getElementById("t33");
    if (fname31.value == "" || ddate32.value == ""  || timeIN33.value == "" ){
        alert("please complete the fill up");
        
    }
        
    else{
        console.log("hahahahah");
            
        let O3 = "Laboratory 3 \n is Occupied by Class \n ";
        let V3 =  document.getElementById("t31") .value;

        var A3 = O3 + V3;


        document.getElementById("b3").innerText = A3;
        document.getElementById("s31").removeAttribute("disabled");
        document.getElementById("t34").removeAttribute("disabled");
        document.getElementById("to3").style.opacity = 1;

        document.getElementById("s32").setAttribute("disabled","disabled");
        document.getElementById("s33").setAttribute("disabled","disabled");
    }
    
    
}
function yes4(){
    var fname41 = document.getElementById("t41");
    var ddate42 = document.getElementById("t42");
    var timeIN43 = document.getElementById("t43");
    if (fname41.value == "" || ddate42.value == ""  || timeIN43.value == "" ){
        alert("please complete the fill up");
        
    }
        
    else{
        console.log("hahahahah");
            
        let O4 = "Laboratory 4 \n is Occupied by Class \n ";
        let V4 =  document.getElementById("t41") .value;
        

        var A4 = O4 + V4;


        document.getElementById("b4").innerText = A4;
        document.getElementById("s41").removeAttribute("disabled");
        document.getElementById("t44").removeAttribute("disabled");
        document.getElementById("to4").style.opacity = 1;

        document.getElementById("s42").setAttribute("disabled","disabled");
        document.getElementById("s43").setAttribute("disabled","disabled");
    }
    
    
}
/////////////////////////////////////////////////////////////////////////////////////////////////*after the last submit*//////////////////////////////////////////////////////////////////////////////////


function sey4(){
    var timeout4 =  document.getElementById("t44");
    if(timeout4.value == ""){
        alert("please complete the fill up");
    }
    else{
        document.getElementById("b4").innerHTML = '<img class="pic" src="desktop-computer.png" alt="image" ><br><h6 class="f">Laboratory 4</h6>';

        
        document.getElementById("s41").setAttribute("disabled","disabled");
        
        document.getElementById("t44").setAttribute("disabled","disabled");
        document.getElementById("to4").style.opacity = 0.1;
        document.getElementById("table4").style.opacity = 0.7;
    }

}




/********************************************************************enabling button in disable function *************************************************************************************************************/



function disable1()
{   
    document.getElementById("s12").removeAttribute("disabled");
    document.getElementById("s13").removeAttribute("disabled");


    document.getElementById("ta1").removeAttribute("disabled");

}

                                          