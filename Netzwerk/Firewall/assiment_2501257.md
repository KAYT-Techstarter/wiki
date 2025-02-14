# Firewall-Anwendung mit iptables auf Ubuntu (WSL)

## 1. Aktuelle Firewall-Regeln anzeigen
### Befehl:
```bash
sudo iptables -S
```
### Bedeutung der Ausgabe:
- **-P INPUT ACCEPT** : Erlaubt eingehende Verbindungen.
- **-P FORWARD ACCEPT** : Erlaubt weitergeleitete Verbindungen.
- **-P OUTPUT ACCEPT** : Erlaubt ausgehende Verbindungen.

---

## 2. HTTP-Anfrage mit curl
### Befehl:
```bash
curl example.com
```
### Beobachtung:
Der HTML-Code der Website wird ausgegeben und kann mit dem Quellcode im Browser verglichen werden.

---

## 3. Ausgehenden Verkehr auf Port 80 blockieren
### Befehl:
```bash
sudo iptables -A OUTPUT -p tcp --dport 80 -j DROP
```
### Erklärung:
- **-A OUTPUT** : Regel für ausgehenden Verkehr.
- **-p tcp** : Betrifft TCP-Verbindungen.
- **--dport 80** : Blockiert Port 80 (HTTP).
- **-j DROP** : Verwirft die Pakete.

### Test:
- **`curl example.com** schlägt fehl.
- Zugriff im Windows-Browser funktioniert weiterhin.

---

## 4. Eingehenden Verkehr auf Port 5000 blockieren
### Befehl:
```bash
sudo iptables -A INPUT -p tcp --dport 5000 -j DROP
```
### Erklärung:
- **-A INPUT** : Regel für eingehenden Verkehr.
- **--dport 5000** : Blockiert Port 5000 (z. B. Flask).

### Test mit Flask:
Kein Zugriff auf `localhost:5000` im Browser möglich.

---

## 5. Firewall-Regeln anzeigen und löschen
### Regeln anzeigen:
```bash
sudo iptables -L --line-numbers
```
### Regeln löschen:
```bash
sudo iptables -D INPUT <Nummer>
sudo iptables -D OUTPUT <Nummer>
```

wichtig die regel numme die die durch **sudo iptables -L --line-numbers** angezeigt werden links
### Überprüfung:
```bash
sudo iptables -S
```