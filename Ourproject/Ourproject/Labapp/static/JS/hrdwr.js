$(document).ready(function(){
    
    document.getElementById("name").addEventListener("keyup", e => {
        if (e.target.value == "" && document.getElementById("PCnum").value == "") {
            document.getElementById("B1").disabled = true;
            alert("please input PC #");
        }
        else {
            document.getElementById("B1").disabled = false;
        }
    })


    $("#y2").click(function(){
        var r1 = $('#tbl_lab1 input:checkbox').length;
        for (var i=0; i<r1; i++){
            if ($('#tbl_lab1 input:checkbox')[i].checked == false)
                alert("Error, Please input data.")
                break
        }
    })
});