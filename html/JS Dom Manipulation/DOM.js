const header = document.getElementById("header");
const body = document.getElementById("body");

headerChangeBack()

function headerChange(time) {
    header.innerHTML = "DOM Manipulation<br><button onclick='headerChangeBack()'>Mach mich rückgängig</button>";  // Text änderung
    header.style.color = "white";
    body.style.backgroundColor = "black";
    header.style.transform = "scale(2.0)";
    header.style.transition = time + "s"; // werte mitgabe durch 3.5 wird zu "3.5s" durch die verkettung
}

function headerChangeBack() {
    header.innerHTML = "DOM Manipulation<br><button onclick='headerChange(1.4)'>Ändere Mich</button>";  // Text änderung
    header.style.color = "black";
    body.style.backgroundColor = "white";
    header.style.transform = "scale(1)";
    header.style.transition = "3.5s";
}

// Scroll Button

const button = document.getElementById("onmouse");

button.onwheel = function (){
    alert("Überroll mich nicht")
}

// eingabe Auslesen

let ausgabefeld = document.getElementById("ausgabeFeld")

function showInputValue (){
   ausgabefeld.innerHTML = document.getElementById("inputField").value
}





