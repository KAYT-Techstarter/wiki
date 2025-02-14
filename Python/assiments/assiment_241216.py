def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y #return gibt die antwort wieder zurück an result

def div(x, y):
    if y != 0: #Ich hatte vorher zur überprufung  y != 0 or x != 0 das hatte zu fehler geführt das die abfrage nicht richtig erfolgen konnte
        return x / y
    else:
        return " ⚠️Error: Division by zero is not allowed⚠️"

def calculator():
    userinput = input("What do you want to do? (add|sub|mult|div): ")
    x = float(input("Tell me the first number: "))
    y = float(input("Tell me the second number: "))

    if userinput == "add":
        result = add(x, y)
    elif userinput == "sub":
        result = sub(x, y)
    elif userinput == "mult":
        result = multiply(x, y)
    elif userinput == "div":
        result = div(x, y)
    else:
        result = "Invalid operation"

    print(f"The result is: {result}")

calculator()
