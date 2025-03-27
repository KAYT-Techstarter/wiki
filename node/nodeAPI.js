const express = require("express");
const app = express();

app.get("/", (req, res) => {
    res.send("Willkommen bei meiner eigenen API!");
});

// Eingabe http://127.0.0.1:3000/
// Ausgabe :
// Willkommen bei meiner eigenen API!


app.get("/data", (req, res) => {
    res.json([
        { id: 1, name: "Max" },
        { id: 2, name: "Lena" }
    ]);
});

// Eingabe http://127.0.0.1:3000/data
// Ausgabe :
// [
//     {
//         "id": 1,
//         "name": "Max"
//     },
//     {
//         "id": 2,
//         "name": "Lena"
//     }
// ]


app.get("/hiKevin", (req, res) => {
    res.json({ message: "Hi Kevin" });
});

// Eingabe http://127.0.0.1:3000/hiKevin
// Ausgabe :
// {
//     "message": "Hi Kevin"
// }

let generateName = require('sillyname');
let sillyName = generateName();

app.get("/randomname", (req, res) => {
    let names = [];
    names.push(generateName());
    res.json(names);
})

// Eingabe http://127.0.0.1:3000/randomname
// Ausgabe :
// [
//     "Micamask Piper",
// ]

app.get("/randomnames", (req, res) => {
    let count = parseInt(req.query.count) || 10; // Standart 10 wenn bei Count nichts mitgeben wurde

    let names = [];
    for (let i = 0; i < count; i++) {
        names.push(generateName());
    }

    res.json(names);
});

// Eingabe http://127.0.0.1:3000/randomname?count=5
// Ausgabe :
// [
//     "Luckshield Goose",
//     "Lovepaw Fang",
//     "Spongethunder Song",
//     "Alabasterweasel Oriole",
//     "Tundraboar Swisher"
// ]

// BONUS WEBSEITEN ANFRAGE ENEGEN NEHMEN

const path = require("path");

app.get("/web", (req, res) => {
    console.log(__dirname);
    res.sendFile(path.join(__dirname, ".", "index.html"));
});

// Eingabe http://127.0.0.1:3000/web
// Ausgabe :
// <!DOCTYPE html>
// <html lang="de">

// <head>
// 	<meta charset="UTF-8">
// 	<meta name="viewport" content="width=device-width, initial-scale=1.0">
// 	<title>Document</title>
// </head>

// <body>
// 	<h1>Ich bin einen webseite die Durch meine api ausgeben wurde ^^</h1>
// </body>

// </html>


app.listen(3000, () => {
    console.log("Server läuft auf http://127.0.0.1:3000&quot;");
});

// funktion start die "API" Port 3000






























// # Erstellen einer einfachen API mit Express

// ## 1. Neues Projektverzeichnis erstellen und Grundkonfiguration

// Öffne die Konsole oder das Terminal und führe folgende Befehle aus:
// ```sh
// mkdir meine-api
// cd meine-api
// npm init -y
// ```

// Dadurch wird ein neues Verzeichnis erstellt und eine `package.json` generiert.

// ### 1.1 Notwendige Pakete installieren

// Installiere Express und das Paket `sillyname` für zufällig generierte Namen:
// ```sh
// npm install express sillyname
// ```
// Falls es Probleme gibt, installiere die Pakete erneut mit:
// ```sh
// npm install
// ```

// ## 2. Erstellen der `index.js` Datei

// Erstelle eine Datei namens `index.js` im Projektverzeichnis und füge folgenden Code hinzu:

// ```js
// const express = require("express");
// const sillyname = require("sillyname");
// const app = express();

// app.get("/", (req, res) => {
//     res.send("Willkommen bei meiner eigenen API!");
// });

// app.get("/data", (req, res) => {
//     res.json([
//         { id: 1, name: "Max" },
//         { id: 2, name: "Lena" }
//     ]);
// });

// app.get("/randomname", (req, res) => {
//     const name = sillyname();
//     res.json({ randomName: name });
// });

// const PORT = 3000;
// app.listen(PORT, () => {
//     console.log(`Server läuft auf http://localhost:${PORT}`);
// });
// ```

// ## 3. Starten der API

// Passe die `package.json` Datei an, indem du den "scripts"-Abschnitt änderst:
// ```json
// "scripts": {
//     "start": "node index.js"
// }
// ```

// Nun kannst du die API starten mit:
// ```sh
// npm start
// ```
// Oder direkt über:
// ```sh
// node index.js
// ```

// Falls du den Fehler "Cannot find module 'express'" bekommst, führe erneut aus:
// ```sh
// npm install express
// ```

// ## 4. Testen der API mit Postman

// ### 4.1 Routen testen
// - **Root Route:** `GET http://localhost:3000/` → Antwort: "Willkommen bei meiner eigenen API!"
// - **Daten Route:** `GET http://localhost:3000/data` → Antwort: JSON mit Namen
// - **Random Name Route:** `GET http://localhost:3000/randomname` → Antwort: Zufälliger Name

// ## 5. (Optional) Weitere Ideen umsetzen
// - **Weitere Routen hinzufügen:** z.B. `/time`, die die aktuelle Zeit zurückgibt.
// - **Middleware verwenden:** z.B. `morgan` für Logging (`npm install morgan`).
// - **Datenbankanbindung:** Einbindung von `MongoDB` oder `SQLite`.

// ## 6. Abgabe
// - Lade dein Projekt auf **GitHub** hoch.
// - Mache einen **Screenshot** von Postman, auf dem die getesteten Routen mit ihren Antworten sichtbar sind.