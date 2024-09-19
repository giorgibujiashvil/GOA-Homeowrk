const password ="giorgi2008";
let pass = prompt("Enter you password");
let attempts = 2;


while(attempts > 0){
    let pass = prompt("Enter your password");
    if(pass !== password){
        attempts --
        alert("you have" + attempts + "left")
    }
    else{
        alert("Access granted")
        break;
    }
    if(attempts === 0){
        alert("system blocked, you have run out of tries")
    }
}