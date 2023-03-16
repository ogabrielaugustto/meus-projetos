const textarea = document.querySelector('textarea')
const finalizar = document.querySelector('.finalizar')


var tipoFila = document.getElementById("tipFila").innerText;


if (tipoFila === 'VERDE'){
    document.getElementById("tipFila").style.color = 'green';
    document.getElementById("tipFila").style.webkitTextStrokeWidth = '1.5px';
    document.getElementById("tipFila").style.webkitTextStrokeColor = 'black';
}

else if (tipoFila === 'VERMELHA'){
    document.getElementById("tipFila").style.color = 'red';
    document.getElementById("tipFila").style.webkitTextStrokeWidth = '1.5px';
    document.getElementById("tipFila").style.webkitTextStrokeColor = 'black';
}

else if (tipoFila === 'AMARELA'){
    document.getElementById("tipFila").style.color = 'yellow';  
    document.getElementById("tipFila").style.webkitTextStrokeWidth = '1.5px';
    document.getElementById("tipFila").style.webkitTextStrokeColor = 'black';

}


let chars = []

finalizar.addEventListener('click', () => {
	var texto = "Finalizou"
	const s = JSON.stringify(texto);
    console.log(s);
    $.ajax({
        url:"/respostaFinalizar",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});
		textarea.value = "Registrado"
        chars = textarea.value.split('')
        window.location.href = "/"	
})

