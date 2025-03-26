const header = document.getElementById("header");
const body = document.getElementById("body");

headerChangeBack()

function headerChange(time) {
    header.innerHTML = "DOM Manipulation<br><button onclick='headerChangeBack(1.4)'>Mach mich rückgängig</button>";  // Text änderung
    header.style.color = "white";
    body.style.backgroundColor = "black";
    header.style.transform = "scale(2.0)";
    header.style.transition = time + "s"; // werte mitgabe durch 3.5 wird zu "3.5s" durch die verkettung
}

function headerChangeBack(time) {
    header.innerHTML = "DOM Manipulation<br><button onclick='headerChange(1.4)'>Ändere Mich</button>";  // Text änderung
    header.style.color = "black";
    body.style.backgroundColor = "white";
    header.style.transform = "scale(1)";
    header.style.transition = time + "s"; // werte mitgabe durch 3.5 wird zu "3.5s" durch die verkettung
}

button1.onmouse = function (){
    alert("Überroll mich nicht")
}



