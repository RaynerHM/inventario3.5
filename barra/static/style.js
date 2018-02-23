/*  ---------------------- Tabla de Articulos ----------------------*/
$(document).ready(function() {
        $('#id_table').DataTable();
} );


/*  ------------------------- Menu SideNav -------------------------*/
$('.deslizar').sideNav({
    menuWidth: 300, // Default is 300
    // edge: 'right', // Choose the horizontal origin
    closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
    draggable: true, // Choose whether you can drag to open on touch screens,
    onOpen: function(el) { /* Do Stuff */ }, // A function to be called when sideNav is opened
    onClose: function(el) { /* Do Stuff */ }, // A function to be called when sideNav is closed
    }
);


/*  ------------------- Confirmar Clave Anterior -------------------*/
var pass_nue = document.getElementById("pass_nue")
var rep_pass = document.getElementById("rep_pass");

function validatePassword(){
  if(pass_nue.value != rep_pass.value) {
    rep_pass.setCustomValidity("¡Las contraseñas no son iguales!");
  } else {
    rep_pass.setCustomValidity('');
  }
}

pass_nue.onchange = validatePassword;
rep_pass.onkeyup = validatePassword;

