#j**2 = -1
#sqrt (-17)
from math import sqrt

result = pow(17, 1/2) *1j
print(result)
print(sqrt(17) * 1j)

x = 1 # przypisanie wartosci do obiektu
result = x == 1 # po równanie wartosci przyjmowanej przez obiekt x z liczba 1

print (x == 1)
print(result)
print (x != 1)
print(result)


name1 = "ala"
name2 = "ala"
print("==", name1 == name2)

name1 = "ala"
name2 = "Ala"
print(">", name1 > name2)

print(ord('a'), ord('A'))
print(ord('a'), ord('n'))

sumaname1 = 0
for i in name1:
        sumaname1 = sumaname1 + ord(i)
print(sumaname1)