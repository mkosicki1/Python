# funckja zwracająca 5 kolejną liczbe pierwszą

#1,2, 3, 5, 7, 11, 13 ...
# n=5-> 11
from datetime import date, datetime, time


def getPrimaryNumbers(n=5): #argument domyslny
    primaryNumbers = [1]
    number = 2
    while(len(primaryNumbers) < n):
        isPrimary = True
        for div in range (2,number):
            if(number % div == 0 ):  # sprawdzenie podzielności
                    isPrimary = False

        if(isPrimary):
            primaryNumbers.append(number)
        number += 1
    return primaryNumbers, primaryNumbers[len(primaryNumbers)-1]


# wywołanie funkcji

element = 11
print("Lista: ", getPrimaryNumbers(element)[0])
print(element, "element:", getPrimaryNumbers(element)[1])
print(getPrimaryNumbers())


#https://docs.python.org/3/library/datetime.html
def printParameters (login, password, email,status=True, registrationDate=date.today()):
    return ("%s %s %s %s %s" % (login, password, email, status, registrationDate))

# rózne wywołania

print(printParameters("mk", "mk", "mk")) # tylko arguumenty obowiazkowe
print(printParameters("mk1", "mk1", "mk1", registrationDate="2020-01-01")) #  arguumenty obowiazkowe
print(printParameters("mk2", "mk2", "mk2", registrationDate="2020-01-01", status=False)) #  arguumenty obowiazkowe

print(printParameters(
    email="mk2",
    password="mk2",
    login="mk2",
    registrationDate="2020-01-01",
    status=False)) #wszytskie elementy

def nonDefinedParameters(*elements): #paramętr gwiazdka -> przyjmuje dowolną liczbe argumentow
    sum=0
    for elem in elements:
        sum += elem
    return sum/len(elements)

print(nonDefinedParameters(1))
print(nonDefinedParameters(5,4,6))
print(nonDefinedParameters(2,2,2,2))


def sortList(numbers):
    numbers.sort()
    return numbers
list = [3,2,5,4,6]
print(sortList(list))


### funkcja bubble sort

def bubbleSort(elements):
    # pętla iterujaca po kolejnych probach sortowania
    noProbes = 1
    for probe in range(len(elements)-1): # determinujemy 5 prób w przypadku najgorszym
                for index, value in enumerate(elements):
                    if(index == len(elements) - 1):
                        break
                    if(elements[index] > elements[index + 1]): # porównywanie sąsiednich komórek
                        elem = elements[index + 1]            # wydobycie elementu na indeksie i +1 do zmiennych
                        elements[index + 1] = elements[index] # zamiana kolejności
                        elements[index] = elem
                print(noProbes,elements)
                noProbes += 1

    return elements
print(bubbleSort([3,2,5,4,6,1]))


def bubbleSort(elements, asc = True):
    # pętla iterujaca po kolejnych probach sortowania
    noProbes = 1
    for probe in range(len(elements)-1): # determinujemy 5 prób w przypadku najgorszym
                isSorted = True
                for index, value in enumerate(elements):
                    if(index == len(elements) - 1):
                        break
                    if((elements[index] > elements[index + 1]) and asc): # porównywanie sąsiednich komórek
                        isSorted = False
                        elem = elements[index + 1]            # wydobycie elementu na indeksie i +1 do zmiennych
                        elements[index + 1] = elements[index] # zamiana kolejności
                        elements[index] = elem

                    if ((elements[index] < elements[index + 1]) and not asc):  # porównywanie sąsiednich komórek
                        isSorted = False
                        elem = elements[index + 1]  # wydobycie elementu na indeksie i +1 do zmiennych
                        elements[index + 1] = elements[index]  # zamiana kolejności
                        elements[index] = elem

                #print(noProbes,elements)
                if(isSorted): # sprawdzenie czy bylismy w if z zmiana elementow
                    break
                noProbes += 1

    return elements

import time

print(bubbleSort([3,2,1,5,4,6, 21,34,44,22,20,55]))
t_start = datetime.now().microsecond
print(bubbleSort([3,2,1,5,4,6, 21,34,44,22,20,55], asc = False))
t_stop = datetime.now().microsecond
print(t_start)
print(t_stop)
print("Czas wykonania funkcji: ", t_stop - t_start)


def bubbleSort(elements):
    # pętla iterujaca po kolejnych probach sortowania
    noProbes = 1
    for probe in range(len(elements)-1): # determinujemy 5 prób w przypadku najgorszym
                isSorted = True
                for index, value in enumerate(elements):
                    if(index == len(elements) - 1):
                        break
                    if(elements[index] > elements[index + 1]): # porównywanie sąsiednich komórek
                        isSorted = False
                        elem = elements[index + 1]            # wydobycie elementu na indeksie i +1 do zmiennych
                        elements[index + 1] = elements[index] # zamiana kolejności
                        elements[index] = elem
                print(noProbes,elements)
                if(isSorted): # sprawdzenie czy bylismy w if z zmiana elementow
                    break
                noProbes += 1

    return elements
print(bubbleSort([3,2,5,4,6,1]))




