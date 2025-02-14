def add(x , y):
    return x + y
def sub(x , y):
    return x - y
def mult(x , y):
    return x * y
def div(x , y):
    if  y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed"
    
def calculator():
    userinput = input("Was möchtest du ausrechnen (add/sub/mult/div): ")
    x = float(input("Zahl Nummer 1: "))
    y = float(input("Zahl Nummer 2: "))

    if userinput == "add":
        result = add(x , y)

    elif userinput == "sub":
        result = sub(x , y)

    elif userinput == "mult":
        result = mult(x , y)

    elif userinput == "div":
        result = div(x , y)
    else:
        result : "Ungültige Eingabe ERROR"

        print(f"Das Ergebnis ist {result}")
    


calculator()