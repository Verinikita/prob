document.addEventListener('DOMContentLoaded', function () {
    // Agrega un evento clic al botón "Upload & Apply"
    document.getElementById('uploadAndApplyButton').addEventListener('click', function () {
        // Obtiene el archivo seleccionado
        const fileInput = document.getElementById('zipFile');
        const file = fileInput.files[0];

        if (file) {
            // Crea una instancia de FormData para enviar el archivo
            const formData = new FormData();
            formData.append('zipFile', file);

            // Crea una instancia de XMLHttpRequest
            const xhr = new XMLHttpRequest();

            // Configura la solicitud AJAX con la ruta correcta de tu servidor Flask
            xhr.open('POST', '/upload', true);

            // Define la función de manejo de la carga exitosa
            xhr.onload = function () {
                if (xhr.status === 200) {
                    // Maneja la respuesta del servidor si es necesario
                    console.log(xhr.responseText);
                    // Cierra el modal después de cargar y aplicar
                    $('#myModal').modal('hide');
                }
            };

            // Define la función de manejo de errores
            xhr.onerror = function () {
                // Maneja errores de la solicitud AJAX
                console.error('Error en la solicitud AJAX');
            };

            // Envía la solicitud AJAX con los datos del formulario
            xhr.send(formData);
        }
    });
});
