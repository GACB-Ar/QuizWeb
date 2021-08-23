const inputNombre=document.getElementById("nombre");
const respuestaC=document.getElementById("respuestaC");

if(inputNombre.getAttribute("value")===respuestaC.getAttribute("value")){
    inputNombre.classList.add("form-input")
}
