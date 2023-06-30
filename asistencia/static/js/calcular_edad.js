document.addEventListener('DOMContentLoaded', function() {
    var fechaNacimientoInput = document.getElementById('id_fecha_de_nacimiento');
    var edadInput = document.getElementById('id_edad');
  
    fechaNacimientoInput.addEventListener('input', function() {
      var fechaNacimiento = new Date(this.value);
      var hoy = new Date();
      var edad = hoy.getFullYear() - fechaNacimiento.getFullYear();
      if (hoy.getMonth() < fechaNacimiento.getMonth() ||
          (hoy.getMonth() === fechaNacimiento.getMonth() && hoy.getDate() < fechaNacimiento.getDate())) {
        edad--;
      }
      edadInput.value = edad;
    });
  });