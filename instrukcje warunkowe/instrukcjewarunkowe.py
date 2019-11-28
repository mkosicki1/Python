### z podanej daty urodzenia wydobywamy rok (yyyy-mm-dd)
# na podstawie obliczonego wieku sprawdź czy uzytkownik jest pełnoletni
# jesli age >=18 to wypisz pełnoletni
#jesli apge < 18 to wypisz niepełnoletni
# jeżeli wiek nie zawiera się w przedziale od 0 do 120 wypisz jestes robotem
# dodatkowo zadba o walidacje wprowadzonych danych
from datetime import date

today = date.today()
birthdate = input("Wprowadź datę urodzenia: ")
year = birthdate[:4]
#sprawdzam czy rok jest liczbą
if(year.isdecimal()):
    #zrzutuj rok na int
    #pass zaslepka
    validYear  = int(year)
    age = today.year -validYear
    if(age >=18  and age <= 120):
        print("Jesteś pełnoletni")
    elif(age < 18 and age >=0):
        print("Jesteś niepełnoletni")
    else:
        print("Jesteś robotem")
else:
    print("Niepoprawna data urodzenia")

### wykorzystujac 3arg sprawdx czy wprowadzona wartosc z klawiatury jest liczbazeli
# jezeli tak wypisz ta liczbe
# jezeli nie wypisz zero

toNumber = input("Podaj liczbę: ")
number = int(toNumber) if toNumber.isdecimal() else 0
print("Wynik działania: ", number)