document.getElementById("getWeatherBtn").addEventListener("click", async function() {
    const place = document.getElementById("place").value.trim();
    
    if (place === "") {
        alert("Mit ganz viel Fantasie und Spangebot hätte das funktioniert 🌈🧽.");
        return;
    }

    try {
        const response = await fetch(`https://wttr.in/${place}?format=%C+%t`);
        const weatherData = await response.text();

        const weatherDiv = document.getElementById("weatherResult");
        weatherDiv.innerHTML = ""; 

        const locationHeading = document.createElement("h2");
        locationHeading.textContent = `Das Wetter in ${place} ist:`;

        const weatherInfo = document.createElement("p");
        weatherInfo.textContent = weatherData;

        weatherDiv.appendChild(locationHeading);
        weatherDiv.appendChild(weatherInfo);
    } catch (error) {
        const weatherDiv = document.getElementById("weatherResult");
        weatherDiv.innerHTML = ""; // Vorherige Inhalte löschen

        const errorMsg = document.createElement("p");
        errorMsg.textContent = "Fehler: Ort nicht gefunden oder ungültige Eingabe";
        weatherDiv.appendChild(errorMsg);
    }
});


  