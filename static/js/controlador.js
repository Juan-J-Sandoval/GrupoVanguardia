
document.getElementById("btn1").addEventListener('click', cambiaValor1)
function cambiaValor1(){
    document.getElementById("nombre").value=document.getElementById("btn1").textContent;
    document.getElementById("urlOculta").value=document.getElementById("btn1").value;
    document.getElementById("conten-bot").src=document.getElementById("btn1").value;
}
document.getElementById("btn2").addEventListener('click', cambiaValor2)
function cambiaValor2(){
    document.getElementById("urlOculta").value=document.getElementById("btn2").value;
    document.getElementById("nombre").value=document.getElementById("btn2").textContent;
    document.getElementById("conten-bot").src=document.getElementById("btn2").value;
}
document.getElementById("btn3").addEventListener('click', cambiaValor3)
function cambiaValor3(){
    document.getElementById("urlOculta").value=document.getElementById("btn3").value;
    document.getElementById("nombre").value=document.getElementById("btn3").textContent;
    document.getElementById("conten-bot").src=document.getElementById("btn3").value;
}
document.getElementById("btn4").addEventListener('click', cambiaValor4)
function cambiaValor4(){
    document.getElementById("urlOculta").value=document.getElementById("btn4").value;
    document.getElementById("nombre").value=document.getElementById("btn4").textContent;
    document.getElementById("conten-bot").src=document.getElementById("btn4").value;
}