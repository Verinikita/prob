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
            xhr.open('POST', 'https://prob-virid.vercel.app/upload', true);

            // Define la función de manejo de la carga exitosa
            xhr.onload = function () {
                if (xhr.status === 200) {
                    // Maneja la respuesta del servidor si es necesario
                    console.log('Éxito:', xhr.responseText);
                    // Cierra el modal después de cargar y aplicar
                    $('#myModal').modal('hide');
                } else {
                    // Muestra mensajes de error en la consola si la solicitud no es exitosa
                    console.error('Error en la solicitud AJAX. Código de estado:', xhr.status);
                }
            };

            // Define la función de manejo de errores de red
            xhr.onerror = function () {
                console.error('Error de red al intentar realizar la solicitud AJAX');
            };

            // Envía la solicitud AJAX con los datos del formulario
            xhr.send(formData);
        } else {
            // Muestra un mensaje si no se seleccionó ningún archivo
            console.error('No se ha seleccionado ningún archivo');
        }
    });
});

            // Envía la solicitud AJAX con los datos del formulario
            xhr.send(formData);
        }
    });
});
