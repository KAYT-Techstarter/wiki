question_date = input("Nenne das Datum, was geprüft werden soll. jjjj.mm.tt = ")

WinterHolidaysStart24 = "2024.12.23"
WinterHolidaysEnd24 = "2025.01.02"
EasterHolidaysStart25 = "2025.04.17"
EasterHolidaysEnd25 = "2025.04.22"
SummerHolidaysStart25 = "2025.08.08"
SummerHolidaysEnd25 = "2025.08.20"
WinterHolidaysStart25 = "2025.12.23"
WinterHolidaysEnd25 = "2026.01.02"

if WinterHolidaysStart24 <= question_date <= WinterHolidaysEnd24:
    print("Das Datum befindet sich in den Winterferien 2024.")
elif EasterHolidaysStart25 <= question_date <= EasterHolidaysEnd25:
    print("Das Datum befindet sich in den Osterferien 2025.")
elif SummerHolidaysStart25 <= question_date <= SummerHolidaysEnd25:
    print("Das Datum befindet sich in den Sommerferien 2025.")
elif WinterHolidaysStart25 <= question_date <= WinterHolidaysEnd25:
    print("Das Datum befindet sich in den Winterferien 2025.")
elif question_date == "2024.10.03":
    print("Das Datum ist der Tag der deutschen Einheit 2024.")
elif question_date == "2025.04.21":
    print("Das Datum ist Ostermontag 2025.")
elif question_date == "2025.05.01":
    print("Das Datum ist der Tag der Arbeit 2025.")
elif question_date == "2025.05.29":
    print("Das Datum ist Christi Himmelfahrt 2025.")
elif question_date == "2025.06.09":
    print("Das Datum ist Pfingstmontag 2025.")
elif question_date == "2025.10.03":
    print("Das Datum ist der Tag der deutschen Einheit 2025.")
elif question_date == "2025.10.31":
    print("Das Datum ist der Reformationstag 2025.")
else:
    print("Es handelt sich um einen regulären Schultag, wenn es gerade ein Montag, Dienstag, Mittwoch, Donnerstag oder Freitag ist 😉")

