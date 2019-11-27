# CTRL + / -> komentarz jednowierszowy
'''
komentarz
wielo-
wierszowy
'''


print('Witaj w Pythonie')
#zmienne -> deklaracja i przypisanie -> inicjalizacja zmiennej(obiektu)
text = "Witaj"
name = "Mirek"
sign = 'a'
print(text + " " + name)

#zmienne na podstawie innych zmiennych
a = 1
b = a +1
print(a,b, (a*b))
print(a, end=';')
print(b, end=';')
print(a+b, end='\n')  #\n - newline
print('www.xyz.pl\\all') #\\ - '\'
print('www.xyz.pl\\\\all') #\\ - '\'
print('"Cytat"')             #
print("I'm Mirek")             #
print("\"Cytat\"")             #


# usuwanie obiektu z pamieci podrecznej
del (a)
#print(a) -

#cw p1

a = 1
b = 2.4
c = "w1"

print(a,b,c)
print(a,b,c, sep='\t')
print(a,b,c, sep='\t\n')
print(a,b,c, sep=' | ')



print(a, end=';')
print(b, end=';')
print(c, end=';')
#cw P2

a = 2.1
b = "abc"
c = 0
print(a,b,c)

#cwiczenie P3

a = 13
b = c
c = 0

print(a,b,c)

#cwiczenie p4

del (a)
del (c)
# c = c + 31.3   -> c is not defined
#print(c )


#cwiczenie P5
name = input("Podaj imię: ") #input zwraca stringa napis
lastname = input("Podaj nazwisko: ") #input zwraca stringa napis
birthdate = input("Podaj datę urodzenia (YYYY-MM-DD): ") #input zwraca stringa napis
possition = input("Podaj stanowisko: ")
salaryNet = float(input("Wprowadź wynagrodzenie netto")) # konwersja string -> float

print(name, lastname, birthdate, possition, salaryNet, salaryNet*1.23, sep=' | ')
print(name, lastname, birthdate, possition, str(salaryNet) + "zł", str(salaryNet*1.23) +"zł", sep=' | ')


## typy zmiennych
name = "Mirek"
salary = 10000.
isActivated = True
element = 1
print(type(name), type(salary), type(isActivated), type(element))


## LICZBY ZESPOLONE

complexNum1 = 2 + 2j
complexNum2 = 5j
realNum1 = 2

print(complexNum1 + complexNum2)
print(complexNum1 + realNum1)
print(type(complexNum1))


### OPERACJE NA LICZBACH

num1 = 1
num2 = 2
print(1/2)
print(type(num1), type(num2),1/2)
print(type(num1), type(num2), 1//2)


print(round(1.5,3))


# KONWERSJA ROZSZERZAJACA I ZAWĘZAJACA
floatNum = 111.9999
floatNum = int(floatNum)  ## konwersja zawezajaca

print(floatNum)

intNum = 5
print(float(intNum))   # konwersja rozszerzajaca


# typ logiczny
print(bool(121), bool(0))
print(bool("dsds"), bool(""))
print(bool(12.2), bool(0.))
print(bool((1,2,3)), bool( () ))


##string

name = "Mirosław"  # string to ciag znaków wystepujacych
print(len(name))
print(name[0])
print(name[len(name) - 1])
print(name[-1])

#print(name[10])
# name(3) = 'k' # string typ niezmienny
#print(name)

name = name + " " + "KOSICKI"
print("ADD: " + name)
name = name[0:8]
print("SUB: "+ name)




####potegowanie

print(8**(1/3))
print(8**(0.33))

x = 1 # przypisanie wartosci do obiektu
x == 1 # po równanie wartosci przyjmowanej przez obiekt x z liczba 1