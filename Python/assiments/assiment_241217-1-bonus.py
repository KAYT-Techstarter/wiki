def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y 

def div(x, y):
    if y != 0: 
        return x / y
    else:
        return " ⚠️Error: Division by zero is not allowed⚠️"

def calc_area():
    x = float(input("Tell me the first Side = "))
    y = float(input("Tell me the second Side = "))
    return x * y

def miles_to_kilometers():
    x = float(input("Tell me how many miles you have to drive: "))
    return x * 1.60934  

def kilometers_to_miles():
    x = float(input("Tell me how many kilometers you have to drive: "))
    return x / 1.60934  

def celsius_to_fahrenheit():
    x = float(input("Tell me how many Celsius do you have: "))
    return (x * 9/5) + 32  

def fahrenheit_to_celsius():
    x = float(input("Tell me how many Fahrenheit do you have: "))
    return (x - 32) * 5/9  

def calculator():
    userinput = input("What do you want to do? (add|sub|mult|div|area|mile2km|km2mile|c2f|f2c): ")
    
    if userinput in ["add", "sub", "mult", "div"]:
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
        elif userinput == "area":
            result = calc_area()
        elif userinput == "mile2km":
            result = miles_to_kilometers()
        elif userinput == "km2mile":
            result = kilometers_to_miles()
        elif userinput == "c2f":
            result = celsius_to_fahrenheit()
        elif userinput == "f2c":
            result = fahrenheit_to_celsius()
        else:
            result = "Invalid operation"

    print(f"The result is: {result}")
    
calculator()
