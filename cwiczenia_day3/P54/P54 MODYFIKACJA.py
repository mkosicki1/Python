## utwórz liste wartosci losowych naturalnych z zakresu 1:100

import random

randomList = []
for x in range(10):
    randomList.append(random.randint(1,10))

print(randomList)

# wyszukaj element z listy i zwróc jego indeks
# jeżeli elementu nie ma na liście to zwróc -1
find = int(input("Podaj liczbę z zakresu od 1 do 10: "))
#sprawdzamy czy element wystepuje w liscie

if(find not in randomList):
        print("Element %i nie występuje na liście" % find)


else:
    for index, value in enumerate(randomList):
        if(value == find):
            print("Element %i znajduje się na indeksie %i" % (find,index))
            break


# sprawdz ile razy dany element znajduje sie na liscie

count = 0
for element in randomList:
    if(element == find):
        count += 1

print("Element %i znajduje się na liście %i razy: " % (find, count))
