import datetime

def current_date_and_time():
    now = datetime.datetime.now()
    return now.strftime("%d.%m.%Y %H:%M:%S")

def days_until_year_end():
    today = datetime.date.today()
    year_end = datetime.date(today.year, 12, 31)
    difference = (year_end - today).days
    return difference

def dayCounter():
    print("Given me the Date from there you want to count since or until today =")
    user_input = input("As DD,MM,YYYY = ")
    target = datetime.datetime.strptime(user_input, "%d,%m,%Y")
    today = datetime.datetime.now ()
    difference = target - today
    return difference.days


def calculate_weekday():
    print("Please enter a date in the format DD.MM.YYYY.")
    date_input = input("Date: ")
    
    if len(date_input) == 10 and date_input[2] == '.' and date_input[5] == '.' and date_input.replace('.', '').isdigit():
        day, month, year = map(int, date_input.split('.'))
        if 1 <= day <= 31 and 1 <= month <= 12:
            target_date = datetime.date(year, month, day)
            return target_date.strftime("%A")
        else:
            return "Invalid date: day or month out of range."
    else:
        return "Invalid date format. Please use DD.MM.YYYY."


def time_in_future():
    now = datetime.datetime.now()

    future_time = now + datetime.timedelta(hours=2)  
    return future_time.strftime("%d.%m.%Y %H:%M:%S")


print("Choose an option:")
print("1: Show current date and time")
print("2: Calculate days until the end of the year")
print("3: Calculate days until a custom date")
print("4: Calculate the weekday of a given date")
print("5: Calculate future date and time based on a time difference")

user_input = input("Choose one of the options = ")

if user_input == "1":
    result = current_date_and_time()
elif user_input == "2":
    result = days_until_year_end()
elif user_input == "3":
    result = dayCounter()
elif user_input == "4":
    result = calculate_weekday()
elif user_input == "5":
    result = time_in_future()
else:
    result = "Invalid input"

print(result)


# def dayCounter():
#     userInput = input("Please enter a date in the format DD.MM.YYYY: ")

#     if len(userInput) == 10 and userInput[2] == '.' and userInput[5] == '.' and userInput.replace('.', '').isdigit():
#         day, month, year = userInput.split('.')

#         if 1 <= int(day) <= 31 and 1 <= int(month) <= 12 and 1 <= int(year) <= 9999:
#             target_date = datetime.datetime.strptime(userInput, "%d.%m.%Y")
#             today = datetime.datetime.today()
#             difference = target_date - today
#             return difference.days
#         else:
#             return "Invalid date: day, month, or year out of range."
#     else:
#         return "Invalid date format. Please use DD.MM.YYYY."


# def calculate_weekday():
#     print("Please enter a date in the format DD.MM.YYYY.")
#     date_input = input("Date: ")
    
#     if len(date_input) == 10 and date_input[2] == '.' and date_input[5] == '.' and date_input.replace('.', '').isdigit():
#         day, month, year = map(int, date_input.split('.'))
#         if 1 <= day <= 31 and 1 <= month <= 12:
#             target_date = datetime.date(year, month, day)
#             return target_date.strftime("%A")
#         else:
#             return "Invalid date: day or month out of range."
#     else:
#         return "Invalid date format. Please use DD.MM.YYYY."

