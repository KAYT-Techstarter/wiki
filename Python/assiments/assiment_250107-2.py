# import requests VORLAGE VON LUKAS

# response = requests.get("https://wttr.in/berlin?format=j1")
# daten = response.json()
# # jetzt sind die json daten in der variable daten gespeichert
# # print(daten)
# # print(daten["current_condition"][0]["temp_C"])
# temperatur = daten["current_condition"][0]["temp_C"]
# wetter = daten["current_condition"][0]["weatherDesc"]
# print(wetter)
# print(f"The weather in Berlin is {wetter} with {temperatur}°C")

import requests

town = input("Give me the name of the Town frome wehre you want the current weather: ")
response = requests.get(f"https://wttr.in/{town}?format=j1")
daten = response.json()
temperatur = daten["current_condition"][0]["temp_C"]
area = daten["nearest_area"][0]["areaName"][0]["value"]
wetter = daten["current_condition"][0]["weatherDesc"][0]["value"]
print(wetter)
print(f"The weather in {town} is {wetter} with {temperatur}°C. The nearest waether station location is {area}")
