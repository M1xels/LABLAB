$(document).ready(function(){
    
    document.getElementById("name").addEventListener("keyup", e => {
        if (e.target.value == "") {
            document.getElementById("submit").disabled = true;
        }
        else {
            document.getElementById("submit").disabled = false;
        }
    })
    $("#y1").click(function(){
        for(i=1; i<=$('#n1').val(); i++){
            $('#row_data').clone(true).appendTo($('#tb1'),('tbody'));

            }
        })
    $("#y2").click(function(){
        var r1 = $('#tbl_lab1 input:checkbox').length;
        for (var i=0; i<r1; i++){
            if ($('#tbl_lab1 input:checkbox')[i].checked != true)
                alert("Error, Please input data.")
                break
        }
    })
});