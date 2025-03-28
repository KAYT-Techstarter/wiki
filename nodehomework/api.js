const express = require("express"); // Import express
const app = express(); // rufe express aus
const fs = require("fs"); // Um dateinen Lesen und Schreiben zu können
const { readFile } = require("fs/promises");
app.use(express.json()); // "Middleware" wird benötigt den Body aus dem Request lesen zu können

// Funktionen um die JSON auslesen zu können

function readData() {
    const data = fs.readFileSync("JSONdatenbank.json", "utf-8");
    return JSON.parse(data); // gebe die Daten aus der JSON aus  
}

function writeData(data) {
    fs.writeFileSync("JSONdatenbank.json", JSON.stringify(data, null, 2)); // Wandel die daten in JSON um eim eintragen
}

app.get("/book", (req, res) => { //LESEN
    const book = readData();
    res.json(book); // gebe deie werde book aus der JSON aus
})

app.post("/book", (req, res) => { //
    const book = readData();
    const { title, author, dataType } = req.body // Lese die datne title und author aus dem body

    if (title && author && author) {
        const newBook = {
            id: book.length + 1,
            title: title,
            author: author,
            dataType: dataType
        }
        book.push(newBook)
        writeData(book)
        res.status(201).json(newBook)
    }
    else {
        res.send("Daten unvollständig")
    }
})

app.put("/book/:id", (req, res) => {
    const id = Number(req.params.id);
    const book = readData();
    const { title, author, dataType } = req.body;

    const foundBook = book.find(b => b.id === id);

    if (title) foundBook.title = title;
    if (author) foundBook.author = author;
    if (dataType) foundBook.dataType = dataType;

    writeData(book);
    res.json(foundBook);
});

// DELETE FUNKTIONIERT NICHT :(

app.delete("/book:id", (req, res) => {
    const id = req.params.id;
    const book = readData();
    const index = book.findIndex(b => b.id === id);

    const remove = book.splice(index, 1)
    
    writeData(book)
    res,json("Das Buch konnte erfolgreich gelöscht werden :" + remove[0].title)
})

app.listen(5555);