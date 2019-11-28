product = {}


id = 1
while(id<=3):

        product[id] = [input("Podaj nazwę produktu: "),
                       int(input("Podaj ilość: ")),
                       float(input("Podaj cenę netto: "))]

        id += 1 # id = id+1

print(product)