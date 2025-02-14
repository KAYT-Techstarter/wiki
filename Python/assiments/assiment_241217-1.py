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

userInput = int(input("Tell me What do you want to do [1=calc_area, 2=miles_to_kilometers, 3=kilometers_to_miles, 4=celsius_to_fahrenheit, 5=fahrenheit_to_celsius]: "))

if userInput == 1:
    result = calc_area()
elif userInput == 2:
    result = miles_to_kilometers()
elif userInput == 3:
    result = kilometers_to_miles()
elif userInput == 4:
    result = celsius_to_fahrenheit()
elif userInput == 5:
    result = fahrenheit_to_celsius()
else:
    result = "Invalid operation"

print(result)
