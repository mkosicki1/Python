sentence = "Ala ma kota, a kot ma Ale."

#oczyść zdanie ze znaków interpunkcyjnych

sentence = sentence.replace(",", "")
sentence = sentence.replace(".", "")
print(sentence)

##zapisz wszytskie słowa w zdaniu w liscie words

words = sentence.split(" ")
print(words)

## listy

params = []
row = [1, "Adam", "Nowak", "2000-01-01", True, 5500.]

# dodawanie parametrów do params

params.append(12.5)
params.append(11.5)
params.append(9.4)

##wypisanie elementow listy

print(params)
print(row)

## zmiana pensji w liscie row

row[5] = 6000.
print(row)
print(row[0:4])

## odczyt elementow z krokiem 2 co 2 element
print(row[0:5:2])

print(row[1:]) # od 2 lelementu

print(row[:3]) # 3 pierwsze elementy
# odwrotna kolejnosc
print(row[:0:-1])
print(row[::-1])

# powielanie list

row = row *2
print(row) # jeden wiersz

#row *= 0 # row = row * 0

print(row)

##długosc listy

print(len(row))

row[6:] = [2, "Jan", "Kowalski", "2001-01-01", False, 10000]
print(row)

##operator przynależnosci

print("Kowalski" in row)
print("Kowalski" not in row)

# konwersja na liste
name = "Mirek"    #
name = list(name)  #edytowalny
name[3] = 'k'
print(name)

# powrot do napisu
string = ""
for v in (name):
    string += str(v);
print(string)   # niezmienny


# lista po kroku
string = ""
for v in (name):
    string += str(v);
    print(string)   # niezmienny

print(name)
name = str(name)
name = name.replace("'","")
name = name.replace(", ","")
name = name.replace("]","")
name = name.replace("[","")
print(name)


numbers = [1,2,3,4,5]
numbers.remove(3)
print(numbers)
deleted = numbers.pop(2) ## usuwanie po indeksie ze zwracaniem
print(numbers)
print(deleted)

numbers = [1,2,3,4,5]
numbers.remove(numbers[3]) ## usuwanie po zawartosci bez zwracania
print(numbers)


## sprawdz czy dwa napisy sa  lustrzane
#sprawdz czy dwie liczby

#1 sposob
text = "kajak"
print(text[ : ]  == text [: : -1])

# 2 sposob
text = list(text)
textRev = text
textRev.reverse()
print(text == textRev)


#sortowanie
nums = [1.1, 2.1, 0.15, 15., 1., 4., 5.]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

names = ["Ala", "Ola", "Ela"]
names.sort()
print(names)


kik = [
            ["_", "_", "_"],
            ["_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"]

      ]

print(kik)
print("lista zewnetrzna",len(kik))
print("pierwszy wiersz", len(kik[0]))
print("drugi wiersz", len(kik[1]))
print("trzeci wiersz", len(kik[2]))
kik[2][3]= "X"
print(kik)
kik [1][1:3] = ["O", "O"]
print(kik)


kik.append(["*", "*", "*"])
print(kik)

kik.insert(0,["*", "*", "*"])
print(kik)
print(len(kik))
kik = [["^", "^", "^"]] + kik
print(kik)

#P34

#twoDim = [[],[]]
#twoDim [0].append(int(input("Podaj pierwszą wartość: ")))
#twoDim [0].append(int(input("Podaj drugą wartość: ")))
#twoDim [0].append(int(input("Podaj trzecią wartość: ")))

#twoDim[1].append(input("Podaj pierwsze imię: "))
#twoDim[1].append(input("Podaj drugie imię: "))
#print(twoDim)

tupleType = (1,2,3,4,5)
#tupleType[1] = 55 # krotka jest typem niezmiennym
print(tupleType)

multiDimTuple = ([1,2], [3,4], [5,6])
#multiDimTuple [0] = 1
multiDimTuple[0].append('X')
multiDimTuple[0][0] = 2
print(multiDimTuple)


a = [1,2]
multiDimTuple = (a, [3,4], [5,6])
#multiDimTuple [0] = 1
multiDimTuple[0].append('X')
multiDimTuple[0][0] = 2
print(multiDimTuple)
a.append(5)
print(multiDimTuple)

print(id(a))
print(id(multiDimTuple[0]))

a1 = 1
a2 = a1
print(id(a1), id(a2))


### SŁOWNIKI

products = {}

## dodanie nowego produktu

products["0x111"] = "Pamięć RAM 8 GB"
products["0x112"] = "Pamięć RAM 16 GB"
products["0x222"] = [1, "PC", "Intel i5 8gen",700]

###modyfikacja pamieci ram
products["0x112"] += " NEW"
products[None] = "AAA"

print(products)
print(products.keys())
print(products.values())


#cwiczenie P39

#liczba= {"jeden": 1, "dwa":2, "trzy":3, "cztery":4, "pięć":5}

#print(liczba(input("Podaj liczbę słownie (1-5): ").lower()))

numberConverter = {"jeden": 1, "dwa":2, "trzy":3, "cztery":4, "pięć":5}
userNumber = input("Podaj Liczbę słownie (1-5)").lower()

if(userNumber in numberConverter):
    print(numberConverter[userNumber])
else:
    print("Podałeś błędną liczbę")


#####ZBIORY

A = set([1,2,3,4,5,6])
B= set([4,5,6,7,8,])


print("Suma", A | B)
print("Część wspólna", A & B)
print("Różnica A-B", A - B)
print("Różnica B-A", B - A)
print("Różnica symetryczna ", B^A )

#dla zdania wprowadzonego przez użytkownika sprawdź ile jest unikatowych słów
#zakładamy że w zdaniu nie występują znaki interpunkcyjne

zdanie = input("Podaj zdanie: ").upper()
words = zdanie.split(" ")
uniqueWords = set(words)
print("Ilość unikatowcych słów: ", len(uniqueWords))
print("Ilość powtórzeń słów: ", len(words)- len(uniqueWords))
