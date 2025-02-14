from flask import Flask

app = Flask(__name__)

# Begrüßungsroute
@app.route("/")
def home():
    return "Willkommen bei meiner Seite von Marvin Young!"

# Route /info
@app.route("/info")
def info():
    return "Dies ist eine einfache API mit Flask."

# Route /team
@app.route("/team")
def team():
    return "Unser Team besteht aus IT-Experten und Entwicklern."

# Route /hilfe
@app.route("/hilfe")
def hilfe():
    return "Hier findest du Unterstützung zu unserer API."

# Route /kontakt
@app.route("/kontakt")
def kontakt():
    return "Schreibe uns eine E-Mail an kontakt@example.com."

# Route /about
@app.route("/about")
def about():
    return "Mein Name ist Max Muster, und ich interessiere mich für Webentwicklung."

# Route /projekt
@app.route("/projekt")
def projekt():
    return "Mein aktuelles Projekt ist eine Flask-API für Anfänger."

# Route /news
@app.route("/news")
def news():
    return "Heute lernen wir, wie man APIs mit Flask erstellt!"

# Route /feedback
@app.route("/feedback")
def feedback():
    return "Wir freuen uns über dein Feedback unter feedback@example.com."

# Route /support
@app.route("/support")
def support():
    return "Besuche unsere Support-Seite unter support.example.com."

# Route /greet mit Parameter <name>
@app.route("/greet/<name>")
def greet(name):
    return f"Hallo {name}, willkommen auf meiner Flask-API!"

if __name__ == "__main__":
    app.run(port=5000)


# Aufagbe 1 Was passiert, wenn die Route / aufgerufen wird?
# Wenn du die Route / aufrufst, zeigt die App den Text "Willkommen bei meiner Flask-App!" an.

# Aufagbe 2 Was geben die Routen /info, /team, /hilfe und /kontakt zurück?
# /info: Zeigt den Text "Dies ist eine einfache API mit Flask."
# /team: Zeigt den Text "Unser Team besteht aus IT-Experten und Entwicklern."
# /hilfe: Zeigt den Text "Hier findest du Unterstützung zu unserer API."
# /kontakt: Zeigt den Text "Schreibe uns eine E-Mail an kontakt@example.com."

# Aufgabe 3 Warum wird app.run(port=5000) verwendet?
# Der Befehl app.run(port=5000) startet die App auf dem Port 5000. Wenn du port=6060 schreibst, startet die App auf Port 6060, also einem anderen Port als dem Standardport.