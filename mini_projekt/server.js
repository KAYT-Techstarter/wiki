const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

app.use(express.json());
app.use(express.static('public'));

const filePath = "ranked.json";

// POST-Request zum Speichern von Daten
app.post('/save', (req, res) => {
    console.log('Empfangene Daten:', req.body);

    // Falls die Datei nicht existiert, erstelle eine leere JSON-Datei
    if (!fs.existsSync(filePath)) {
        fs.writeFileSync(filePath, JSON.stringify([], null, 2), 'utf8');
    }

    // Lese die bestehende JSON-Datei
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            console.error("Fehler beim Lesen der Datei:", err);
            return res.status(500).json({ error: "Fehler beim Lesen der Datei" });
        }

        let list;
        try {
            // Versuche, die Datei als JSON zu parsen
            list = JSON.parse(data);
        } catch (parseError) {
            console.error("Fehler beim Parsen der JSON-Datei:", parseError);
            return res.status(500).json({ error: "Fehler beim Parsen der Datei" });
        }

        // Neuen Eintrag aus dem Request-Body hinzufügen
        const newEntry = req.body;
        list.push(newEntry);

        // Schreibe die aktualisierte Liste zurück in die Datei
        fs.writeFile(filePath, JSON.stringify(list, null, 2), 'utf8', (err) => {
            if (err) {
                console.error('Fehler beim Schreiben der Datei:', err);
                return res.status(500).json({ error: 'Fehler beim Schreiben der Datei' });
            }
            console.log('Neuer Eintrag erfolgreich gespeichert:', newEntry);
            res.status(201).json({ message: 'Eintrag erfolgreich gespeichert' });
        });
    });
});

// GET-Request zum Abrufen aller gespeicherten Daten
app.get('/data', (req, res) => {
    // Falls die Datei nicht existiert, gib eine leere Liste zurück
    if (!fs.existsSync(filePath)) {
        return res.json([]);
    }

    // Lese die JSON-Datei
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            console.error("Fehler beim Lesen der Datei:", err);
            return res.status(500).json({ error: "Fehler beim Lesen der Datei" });
        }

        try {
            // JSON parsen und zurücksenden
            const list = JSON.parse(data);
            res.json(list);
        } catch (parseError) {
            console.error("Fehler beim Parsen der Datei:", parseError);
            res.status(500).json({ error: "Fehler beim Parsen der Datei" });
        }
    });
});

// Server starten
app.listen(port, () => {
    console.log(`✅ Server läuft auf http://localhost:${port}`);
});
