var currentNumberWrapper = document.getElementById("currentNumber");
var currentNumber = 0;

function increment(){
    currentNumber = currentNumber + 1;
    currentNumberWrapper.innerHTML = currentNumber;
}

function decrement(){
    if (currentNumber >= 0){
        currentNumber = currentNumber - 1;
        currentNumberWrapper.innerHTML = currentNumber; 
    }
    else{
        currentNumber = currentNumber * 0;
        currentNumberWrapper.innerHTML = currentNumber; 
    }
}

function reset(){
    currentNumber = currentNumber * 0;
    currentNumberWrapper.innerHTML = currentNumber;
}

