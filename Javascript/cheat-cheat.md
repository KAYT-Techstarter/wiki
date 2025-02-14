***Python vs. JavaScript - Cheatsheet***

**Python:**
```python
x = 10
y = "Hallo"
print(x, y)
```

**JavaScript:**
```javascript
let x = 10;
let y = "Hallo";
console.log(x, y);
```

---
### 2. Funktionen
**Python:**
```python
def begruessung(name):
    return f"Hallo, {name}!"

print(begruessung("Marvin"))
```

**JavaScript:**
```javascript
function begruessung(name) {
    return `Hallo, ${name}!`;
}

console.log(begruessung("Marvin"));
```

---
### 3. Klassen
**Python:**
```python
class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def vorstellen(self):
        return f"Ich bin {self.name} und {self.alter} Jahre alt."

p = Person("Marvin", 25)
print(p.vorstellen())
```

**JavaScript:**
```javascript
class Person {
    constructor(name, alter) {
        this.name = name;
        this.alter = alter;
    }

    vorstellen() {
        return `Ich bin ${this.name} und ${this.alter} Jahre alt.`;
    }
}

const p = new Person("Marvin", 25);
console.log(p.vorstellen());
```

---
### 4. Schleifen
**Python:**
```python
for i in range(5):
    print(i)
```

**JavaScript:**
```javascript
for (let i = 0; i < 5; i++) {
    console.log(i);
}
```

**While-Schleife:**
**Python:**
```python
x = 0
while x < 5:
    print(x)
    x += 1
```

**JavaScript:**
```javascript
let x = 0;
while (x < 5) {
    console.log(x);
    x++;
}
```

---
### 5. Bedingte Anweisungen
**Python:**
```python
x = 10
if x > 5:
    print("x ist größer als 5")
elif x == 5:
    print("x ist genau 5")
else:
    print("x ist kleiner als 5")
```

**JavaScript:**
```javascript
let x = 10;
if (x > 5) {
    console.log("x ist größer als 5");
} else if (x === 5) {
    console.log("x ist genau 5");
} else {
    console.log("x ist kleiner als 5");
}
```

---
### 6. Listen & Arrays
**Python:**
```python
zahlen = [1, 2, 3, 4, 5]
print(zahlen[0])
```

**JavaScript:**
```javascript
let zahlen = [1, 2, 3, 4, 5];
console.log(zahlen[0]);
```

---
### 7. Dictionaries & Objects
**Python:**
```python
person = {"name": "Marvin", "alter": 25}
print(person["name"])
```

**JavaScript:**
```javascript
let person = { name: "Marvin", alter: 25 };
console.log(person.name);
```

---
### 8. Exception Handling
**Python:**
```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Fehler: Division durch Null")
```

**JavaScript:**
```javascript
try {
    console.log(10 / 0);
} catch (error) {
    console.log("Fehler: Division durch Null");
}
```

---
### 9. Taschenrechner mit Nutzereingabe
**Python:**
```python
num1 = float(input("Gib die erste Zahl ein: "))
operator = input("Gib den Operator ein (+, -, *, /): ")
num2 = float(input("Gib die zweite Zahl ein: "))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print("Ungültiger Operator")
```

**JavaScript:**
```javascript
const num1 = parseFloat(prompt("Gib die erste Zahl ein:"));
const operator = prompt("Gib den Operator ein (+, -, *, /):");
const num2 = parseFloat(prompt("Gib die zweite Zahl ein:"));

let result;
switch (operator) {
    case '+':
        result = num1 + num2;
        break;
    case '-':
        result = num1 - num2;
        break;
    case '*':
        result = num1 * num2;
        break;
    case '/':
        result = num1 / num2;
        break;
    default:
        result = "Ungültiger Operator";
}
alert(result);
```

---
Das sind die grundlegenden Unterschiede zwischen Python und JavaScript! 🚀

