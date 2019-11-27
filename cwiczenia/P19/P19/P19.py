name = input("Podaj imię: ") #input zwraca stringa napis
lastname = input("Podaj nazwisko: ") #input zwraca stringa napis
birthdate = input("Podaj date urodzenia: ") #input zwraca stringa napis
possition = input("Podaj stanowisko: ")
salaryGR = float(input("Wprowadź wynagrodzenie brutto: ")) # konwersja string -> float

print("Pan " + name + " " + lastname + "(ur." + birthdate + ") ")
print("Wiek: " + str(2019 - int(birthdate[0:4])))
print("Stanowisko: " + possition)
print("Wynagrodzenie BRUTTO: " + str(round(salaryGR,2)) + " zł")

