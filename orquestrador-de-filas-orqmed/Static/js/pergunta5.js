const textarea = document.querySelector('textarea')
const btnfem = document.querySelector('.btnfem')
const btnman = document.querySelector('.btnman')

let chars = []

btnfem.addEventListener('click', () => {
	var texto = "F"
	const s = JSON.stringify(texto);
    console.log(s);
    $.ajax({
        url:"/resposta5",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});
		textarea.value = "Registrado"
        chars = textarea.value.split('')
        window.location.href = "/pergunta6"
		
})

btnman.addEventListener('click', () => {
	var texto = "M"
	const s = JSON.stringify(texto);
    console.log(s);
    $.ajax({
        url:"/resposta5",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});
		textarea.value = "Registrado"
        chars = textarea.value.split('')
        window.location.href = "/pergunta6"
		
})



