function consult_user(){
    id = document.getElementById('ident').value
    fetch('/consult_user', {
        "method":"post",
        "headers":{"Content-Type":"application/json"},
        "body": JSON.stringify(id)
    })
    .then(resp => resp.json())
    .then(data => {
        document.getElementById("txt-response").value = data.name + " " + data.lastname + " " + data.project + " "+ data.hour + " " + data.date
        document.getElementById("img-user").src = "https://bucket-bitacora.s3.us-east-2.amazonaws.com/bitacora/" + id + ".jpg"
                                                
    })
    
}