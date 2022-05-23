$(document).ready(function(){

    

    $("#Save").click(function(){
        var r1 = $('#tbl_report select').length;
        alert(r1)
        for (var i=0; i<r1; i++){
            if ($('#tbl_report select')[i].value == "Available to use"){
                $('#tbl_report tr')[i+1].remove()
            }
        }
    })
    
});