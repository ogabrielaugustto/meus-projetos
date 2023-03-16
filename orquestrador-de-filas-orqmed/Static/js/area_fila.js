const textarea = document.querySelector('textarea')
const btnido = document.querySelector('.btnido')
const btnges = document.querySelector('.btnges')
const btndef = document.querySelector('.btndef')
const btnnao = document.querySelector('.btnnao')

let chars = []

btnido.addEventListener('click', () => {
	var texto = "Idoso"
	const s = JSON.stringify(texto);
    console.log(s);
    $.ajax({
        url:"/respostaAreaFila",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});
		textarea.value = "Anotado!"
        chars = textarea.value.split('')
        window.location.href = "/pergunta7"
		
})

btnges.addEventListener('click', () => {
	var texto = "Gestante"
	const s = JSON.stringify(texto);
    console.log(s);
    $.ajax({
        url:"/resposta6",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});
		textarea.value = "Enviado"
        chars = textarea.value.split('')
        window.location.href = "/pergunta7"
		
})

btndef.addEventListener('click', () => {
	var texto = "PcD"
	const s = JSON.stringify(texto);
    console.log(s);
    $.ajax({
        url:"/resposta6",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});
		textarea.value = "Enviado"
        chars = textarea.value.split('')
        window.location.href = "/pergunta7"
		
})

btnnao.addEventListener('click', () => {
	var texto = "Nao"
	const s = JSON.stringify(texto);
    console.log(s);
    $.ajax({
        url:"/resposta6",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});
		textarea.value = "Enviado"
        chars = textarea.value.split('')
        window.location.href = "/pergunta7"
		
})



