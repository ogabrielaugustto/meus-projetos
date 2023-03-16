var btn_play = document.querySelector('#btn-play');
var btn_stop = document.querySelector('#btn-stop');
document.getElementById('btn-stop').style.display = 'none';

if(window.SpeechRecognition || window.webkitSpeechRecognition){
	console.log('ok');
	var API = window.SpeechRecognition ||  window.webkitSpeechRecognition;

	var recognition = new API();

	recognition.continuous = 'true';
	recognition.lang = 'pt-BR';


	
	recognition.onstart = function(){
		console.log('botao start');
		document.getElementById('areatexto').innerHTML = "Estou ouvindo...";
	};

	recognition.onresult= function(e){
		console.log(e.results[0][0].transcript);
		

		for(var i =e.resultIndex; i<e.results.length; i++){

			var resultado = e.results[i][0].transcript;
			
			document.getElementById('areatexto').innerHTML = "Você disse:  " + resultado +". Se estiver de acordo, pode avançar!";
			
		}

    
    const s = JSON.stringify(resultado);
    console.log(s);

    $.ajax({
        url:"/resposta8",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});
  
	};


	recognition.onend=function(){
		console.log('botao Stop');
	};

	btn_play.addEventListener('click',function(){
		recognition.start();
		document.getElementById('btn-stop').style.display="inline";
		document.getElementById('btn-play').style.display="none";
	},false);

	btn_stop.addEventListener('click',function(){
		recognition.stop();
 
		document.getElementById('btn-play').style.display="inline";
		document.getElementById('btn-stop').style.display="none";
	},false );

  
}else{
	console.log('error');
}

const btnnao = document.querySelector('.btnnao')
btnnao.addEventListener('click', () => {
	var texto = "Nao"
	const s = JSON.stringify(texto);
    console.log(s);
    $.ajax({
        url:"/resposta8",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});
		textarea.value = "Registrado"
        chars = textarea.value.split('')
        window.location.href = "/pergunta9"
		
})
