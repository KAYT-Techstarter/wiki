# Flask wird importiert, um eine Webanwendung zu erstellen. `request` wird genutzt, um HTTP-Requests zu verarbeiten, und `jsonify`, um JSON-Antworten zurückzugeben.
from flask import Flask, request, jsonify  

# Aufruf einer simulierten externen Datenbank im übergeordneten Verzeichnis /External/users_list.py
from External.users_list import users

# HTTP Condes
# 200 - Alles Gut
# 400 - Problem mit der Anfrage
# 500 - Iregndwas im Code läuft schief
# 404 - Seite nicht erreichbar

# Flask-Anwendung initialisieren
app = Flask(__name__)

# Interne simulierte Datenbank mit Produkten
products = [
    {"id": 1, "name": "laptop", "price": 1200},
    {"id": 2, "name": "tv", "price": 800},
    {"id": 3, "name": "laptop", "price": 1200},
    {"id": 4, "name": "tv", "price": 1200},
    {"id": 5, "name": "laptop", "price": 1200},
]

# Standardroute der Anwendung
# Eingabe: http://127.0.0.1:5000
# Ausgabe: Willkommen bei meiner Seite von cheat sheet Flask
@app.route("/")
def home():
    return "Willkommen bei meiner Seite von cheat sheet Flask"

# Informationsroute
# Eingabe: http://127.0.0.1:5000/info
# Ausgabe: Dies ist eine einfache API mit Flask.
@app.route("/info")
def info():
    return "Dies ist eine einfache API mit Flask."

# Begrüßungsroute mit Namensplatzhalter
# Eingabe: http://127.0.0.1:5000/greet/Marvin
# Ausgabe: Hallo Marvin, willkommen auf meiner Flask-API!
@app.route("/greet/<name>")
def greet(name):
    return f"Hallo {name}, willkommen auf meiner Flask-API!"

# Route mit Platzhalter und und zusätzlichen Parameter
# Eingabe: http://127.0.0.1:5000/brand/21?type=clothes&condition=new
# Ausgabe: Brand-ID: 21, Type: clothes, Condition: new
@app.route('/brand/<id>')
def brand(id):
    type_ = request.args.get('type')  
    condition = request.args.get('condition')  
    return f"Brand-ID: {id}, Type: {type_}, Condition: {condition}"

# Suchroute mit zusätzlichen Parameter
# Eingabe: http://127.0.0.1:5000/search?query=black
# Ausgabe: Searching for: black
@app.route('/search')
def search():
    query = request.args.get('query')  
    return f"Searching for: {query}"

# Route zur Filterung der Produktdatenbank Zeile 11 Interne Simulierte Datenbank
# Eingabe: http://127.0.0.1:5000/products?name=laptop
# Ausgabe: Gefilterte Liste der Produkte, die den Namen "laptop" enthalten
@app.route("/products", methods=["GET"])
def get_products():
    name_filter = request.args.get("name")
    if name_filter:
        filtered_products = [
            p for p in products if name_filter.lower() in p["name"].lower()
        ]
        return jsonify(filtered_products), 200  
    return jsonify(products), 200  # Liste Wird in JSON vormat zurück gegeben Diese Funktion muss in Zeiel 1 Aufgerufen werden damit das möglich ist.

#______________________________________________________________________________________________________
# Ab Hier Komme ich nicht mehr weiter 

# FRAGE WO HOLT SICH DER CODE INFO DAS ER IN EXTERNAL:USER_LIST.py SCAHUEN SOLL?

# Route zur Benutzersuche in der externen Simuliereten Datenbank
# Eingabe: http://localhost:5000/search?name=Charlie
# Rückgabe: "Found user: Charlie" oder "No user found with name: Charlie"
@app.route("/search", methods=["GET"])
def get_user_by_name():
    final_user = None  
    name = request.args.get("name")  
    for u in users:
        if u["firstName"] == name:  
            final_user = u

    if final_user is None:
        return "User could not be found "  

    return f"The User is {final_user}" 

#______________________________________________________________________________________________________
# Ab Hier Komme ich nicht mehr weiter 
# Ich alles unten POSTEMAN gemacht bekomme aber die Meldung 500 zurück

# Hierzu wird POSTMAN BENÖTIGT
# Eingabe: localhost:5000/users/login
# Body: 
# Auf RAw schalten
# Text Art JSON
# Inahlt ↓
# # {
#   "username": "maexchen", 
#   "password": "letsGo"
#}
# Ausgabe :
@app.route("/users/login", methods=["POST"])
def login():
    credentials = request.get_json()  # JSON-Daten aus der Anfrage auslesen
    username = credentials["username"]
    password = credentials["password"]

    final_user = None 
    for u in users:
        if u["username"] == username:  #
            final_user = u

    if final_user is None:
        return "User could not be found "

    return f"Hallo {credentials} {username} {password}"


# Diese Bedingung sorgt dafür, dass das Programm nur ausgeführt wird, und mit app = Flask(__name__) auch initialiesiert beleibt
if __name__ == "__main__":
    # Die Anwendung auf Port 5000 mit aktiviertem Debug-Modus starten
    # Debug=True sorgt dafür, dass Änderungen automatisch neu geladen werden, ohne die Anwendung manuell neu zu starten.
    # Der Port sag aus auf welchem port das programm hören soll um anfragen endgegegen zu nehmen
    app.run(port=5000, debug=True)
