function myFunctionMill() {
document.getElementById("myDropdownMill").classList.toggle("show");
}
function myFunctionTurn() {
document.getElementById("myDropdownTurn").classList.toggle("show");
}

window.onclick = function(event) {
if (!event.target.matches('.dropbtn')){
var dropdowns = document.getElementsByClassName("dropdown-content");
var i;
for(i = 0; i<dropdowns.length; i++){
var openDropdown = dropdown[i];
if (openDropdown.classList.contains('show')){
openDropdown.classList.remove('show')
}
}
}
}
