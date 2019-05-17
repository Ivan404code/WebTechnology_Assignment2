function validation(){
    var name=document.getElementById("name").value;
    var town=document.getElementById("town").value;
    var mail=document.getElementById("mail").value;
    var phone=document.getElementById("phone").value;
    if(name=="" || town=="" || mail=="" || phone=="")
    {
        document.getElementById("result").innerHTML="All fields are required.";
        return false;
    }
    else if(name.length<2){
        document.getElementById("result").innerHTML =" Name must have a minimum of 2 characters."
        
    }
    else if(phone.length !==11){
        document.getElementById("result").innerHTML="This field requires 11 digits."
    }
    else{
        return true;
        
    }
}

