function seterror(index, error){
    // const element = document.getElementById(id);
    document.getElementsByClassName('form-error')[index].innerHTML = error;
}
function validationForm(){
    let returnval = false;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const email = document.getElementById('email').value;
    const firstname = document.getElementById('firstname').value;
    const lastname = document.getElementById('lastname').value;
    const phonenumber = document.getElementById('phonenumber').value;

    const inputObj = {
        username:0,
        password:1,
        email:2,
        firstname:3,
        lastname:4,
        phonenumber:5,
    }
    usernameRex = new RegExp('^[a-z A-z _]+')
    passwordRex = new RegExp('^[a-z A-z 0-9 $@!$%^&*!~]{8,}')
    emailRex = new RegExp('[a-z A-z 0-9 _ \-]+[@][a-z]+[\.][a-z]{2,3}')
    firstname = new RegExp('^[a-z A-z]{1,15}')
    lastname = new RegExp('^[a-z A-z]{1,15}')
    phonenumber = new RegExp('[9876][0-9]{9}')
    let check = true;
    if(!usernameRex.test(username)){
        seterror(inputObj.username,"username can not start with numbers or special character or can not be blank.")
        check = false
    }
    else if(!passwordRex.test(password)){
        seterror(inputObj.password,"Password must be longer then 8 characters and must contain specail characters (ex: !@#$%^&*).")
        check = false
    }
    else if(!emailRex.test(email)){
        seterror(inputObj.email,"Email is not correct.")
        check = false
    }
    else if(!firstname.test(email)){
        seterror(inputObj.firstname,"First name must be alphabetic.")
        check = false
    }
    else if(!lastname.test(email)){
        seterror(inputObj.lastname,"Last name must be alphabetic.")
        check = false
    }
    else if(!lastname.test(email)){
        seterror(inputObj.phonenumber,"Phonenumber is not correct.")
        check = false
    }
    else{
        returnval = true
        console.log("Success.")
    }
   return returnval;
}