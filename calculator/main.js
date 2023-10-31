const input = document.getElementById("input");
const temp = document.getElementById("tmp");
const empty = (element)=>{
    element.innerText = "";
};
document.getElementById("all-clear",addEventListener("click",()=>{
    empty(temp);
    empty(input);
}));
document.querySelectorAll(".number",addEventListener("click",()=>{
    console.log()
}));
