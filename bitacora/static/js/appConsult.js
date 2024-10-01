function consult_user() {
    const id = document.getElementById('ident').value;
    const loadingElement = document.getElementById('loading');
    const imgElement = document.getElementById('img-user');
    const responseElement = document.getElementById('txt-response');
    
    // Mostrar indicador de carga
    loadingElement.style.display = 'block';
    
    fetch('/consult_user', {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(id)
    })
    .then(resp => resp.json())
    .then(data => {
        // Ocultar indicador de carga
        loadingElement.style.display = 'none';
        
        // Actualizar la imagen y el textarea
        responseElement.value = `${data.name} ${data.lastname} ${data.project} ${data.hour} ${data.date}`;
        imgElement.src = `https://bucket-bitacora.s3.us-east-2.amazonaws.com/bitacora/${id}.jpg`;
        imgElement.style.display = 'block';  // Mostrar la imagen
    })
    .catch(error => {
        // Manejo de errores
        loadingElement.style.display = 'none';
        responseElement.value = "Error al consultar el usuario.";
        imgElement.style.display = 'none';
    });
}
