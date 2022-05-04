$(document).ready(function(){
    
    $('#monitoring').click(function(){
        $('#Monitoring').show()
        $('#Equipment_Device').hide()
        $('#Reports').hide()
        document.getElementById("equipment_Device").classList.remove("active")
        document.getElementById("monitoring").classList.add("active")
        document.getElementById("reports").classList.remove("active")
        
    })
    $('#equipment_Device').click(function(){
        $('#Monitoring').hide()
        $('#Equipment_Device').show()
        $('#Reports').hide()
        document.getElementById("equipment_Device").classList.add("active")
        document.getElementById("monitoring").classList.remove("active")
        document.getElementById("reports").classList.remove("active")
    })
    $('#reports').click(function(){
        $('#Monitoring').hide()
        $('#Equipment_Device').hide()
        $('#Reports').show()
        document.getElementById("reports").classList.add("active")
        document.getElementById("equipment_Device").classList.remove("active")
        document.getElementById("monitoring").classList.remove("active")
    })
    
});

