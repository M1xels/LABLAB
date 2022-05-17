$(document).ready(function(){
        

        $("#table1").show();

        document.getElementById("h1").disabled = true;
        $("#slct1").click(function(){
            var r1 = $('#tbl_lab1 input:checkbox').length;
            for (var i=0; i<r1; i++){
                $('#tbl_lab1 input:checkbox')[i].checked = true;
                }
        })
    
    
        
    
        $("#h1").click(function(){


            $("#edata1").show();
            $("#edata2").hide();
            $("#edata3").hide();
            $("#edata4").hide();
    
            document.getElementById("h1").disabled = true;
            document.getElementById("h2").disabled = false;
            document.getElementById("h3").disabled = false;
            document.getElementById("h4").disabled = false;
            
        });
        $("#h2").click(function(){

    
            $("#table2").show();
            document.getElementById("h3").disabled = true;
            $("#slct2").click(function(){
                var r1 = $('#tbl_lab2 input:checkbox').length;
                for (var i=0; i<r1; i++){
                    $('#tbl_lab2 input:checkbox')[i].checked = true;
                    }
            })
        

            $("#edata1").hide();
            $("#edata2").show();
            $("#edata3").hide();
            $("#edata4").hide();
    
            
            document.getElementById("h1").disabled = false;
            document.getElementById("h2").disabled = true;
            document.getElementById("h3").disabled = false;
            document.getElementById("h4").disabled = false;
    
        });
        $("#h3").click(function(){
            $("#table3").show();
            document.getElementById("h3").disabled = true;
            $("#slct3").click(function(){
                var r1 = $('#tbl_lab3 input:checkbox').length;
                for (var i=0; i<r1; i++){
                    $('#tbl_lab3 input:checkbox')[i].checked = true;
                    }
            })

            $("#edata1").hide();
            $("#edata2").hide();
            $("#edata3").show();
            $("#edata4").hide();
    
            document.getElementById("h1").disabled = false;
            document.getElementById("h2").disabled = false;
            document.getElementById("h3").disabled = true;
            document.getElementById("h4").disabled = false;
    
        });
        $("#h4").click(function(){
            $("#table4").show();

            document.getElementById("h4").disabled = true;
            $("#slct4").click(function(){
                var r1 = $('#tbl_lab4 input:checkbox').length;
                for (var i=0; i<r1; i++){
                    $('#tbl_lab4 input:checkbox')[i].checked = true;
                    }
            })
            $("#edata1").hide();
            $("#edata2").hide();
            $("#edata3").hide();
            $("#edata4").show();
    
            
            document.getElementById("h1").disabled = false;
            document.getElementById("h2").disabled = false;
            document.getElementById("h3").disabled = false;
            document.getElementById("h4").disabled = true;
    
        });
    });