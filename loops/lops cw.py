elements = range(5,50,1)
index = 0

while(True):
    print(index, elements[index])
    index += 1   # inkrementacja indeksu
    if(index == 13): # warunek przerwania
        break; # przerwanie natychmiastowe wyjscie z petli

elements = range(5, 50, 1)
index = -1

while(index < len(elements)):
    index+= 1  # inkrementacja indeksu
    if(index % 2 == 0):
        continue # pominiecie literacji
    print(index, elements[index])
    if (index == 13):  # warunek przerwania
                break;  # przerwanie natychmiastowe wyjscie z petli

### wprowadź dane z klawiatury do listy tak długo az user wpisze q
elements = []
flag = True
while(True):
    elem = input("Podaj wartość lub wprowadź Q zeby wyjść: ")
    if (elem.upper() == "Q"):
        print("wyjście")
        break
    elements.append(elem)
print(elements)

elements = []
while(flag):
    elem = input("Podaj wartość lub wprowadź Q zeby wyjść: ")
    if (elem.upper() == "Q"):
        print("wyjście")
        flag = not flag
        continue
    elements.append(elem)
print(elements)