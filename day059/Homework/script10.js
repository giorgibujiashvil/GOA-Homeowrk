
const form = document.getElementById("form")
const result = document.getElementById("result")

form.addEventListener("submit", function(e){
    e.preventDefault();

    if(firstname.value.length < 1 || email.value.length < 1 || pass.value.length < 1){
        result.innerHTML = "Empty Input"
    }else{
        result.innerHTML = "Correct"
    }
})