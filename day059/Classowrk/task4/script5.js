const messagebox = document.getElementById("message")
const countbox = document.getElementById("count")

messagebox.addEventListener("input",counter)

function counter(){
    const limit = 200;
    let current_count = messagebox.value.length

    if(current_count > limit){
    countbox.style.color = "red"
    countbox.textContent ="Character limit exceeded"

    }
    else{
        countbox.style.color = "green"
        countbox.textContent = current_count + "/" + limit
    }

}

