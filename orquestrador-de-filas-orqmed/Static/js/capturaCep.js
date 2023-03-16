const buttons = document.querySelectorAll('.btn')
const textarea = document.querySelector('textarea')

const delete_btn = document.querySelector('.delete')
const shift_btn = document.querySelector('.shift')
const space_btn = document.querySelector('.space')
const btn_enter = document.querySelector('.enter')

let chars = []
textarea.value = ''

buttons.forEach(btn => {
    btn.addEventListener('click', () => {
        textarea.value += btn.innerText
        chars = textarea.value.split('')

		let inputLength = textarea.value.length
        if (inputLength == 05) {
			textarea.value += '-'
        }
        if (textarea.value.length >= 9){
            textarea.value = textarea.value.substring(0, 9)
        }
        
    }) 
 
})
document.querySelector('textarea').maxLength = '9';

delete_btn.addEventListener('click', () => {
    chars.pop()
    textarea.value = chars.join('')
})

btn_enter.addEventListener('click', () => {
	var texto = textarea.value
	const s = JSON.stringify(texto);
    console.log(s);
    $.ajax({
        url:"/respostaCep",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});
		textarea.value = "Enviado"
        chars = textarea.value.split('')
        window.location.href = "/NumLogradouro"
		
})



