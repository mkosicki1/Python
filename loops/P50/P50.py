
#SLOWNIK ID -> LISTA CECH
products = {"1": ["A",3.5, 10],
            "2": ["B",2.99, 5],
            "3": ["C",9.99, 1]}

## KOSZYK ZAWIERA LISTY ZAMÓWIONYCH PRODUKTÓW

basket = []
cumSum = 0
# CLI UŻYTKOWNIKA

while(True):
    # PETLA WYPISUJACA PRODUKTY
    print("| %3s | %8s | %10s | %5s |"

           % ("id","Produkt","Cena", "Ilość"))
    for key in products.keys():
       # print(key, products[key])###|id |nazwa| |cena| ilość m|
        print("| %3s | %8s | %8.2fzł | %5.1f |" %
              (key, products[key][0], products[key][1], products[key][2]))

    # pobieranie danych od użytkonika
    choice = input("Co chcesz zamówić, podaj id produktu lub Q-wyjscie")
    # wyjście z programu
    if(choice.upper() == "Q"):
        print("Wyjście")
        break
    # sprawdzenie czy istnieje taki id
    if(choice not in products.keys()):
        print("nie ma takiego produktu")
        continue

    while(True):
        # łapanie wyjatku gdy uzytkownik wprowadzi wartosc nieliczbowa
        try:
            quantity = float(input("Wprowadź ilość zamawianego produktu:"))
        except:
            print("błedny typ danych wprowadz liczbe!")
            continue

    # sprawdzenie dostepnosci produktu

        if(quantity > products[choice][2] and quantity >= 0):
            print("Dostepnych jest tylko: " +  str(products[choice][2]) + "szt.")
            continue
        else:
            break

    ##aktualizacja magazynu i koszyka
    products[choice][2] -= quantity #products[choice][2] = products[choice][2] - quantity
    basket.append([products[choice][0], products[choice][1], quantity])
    #suma skumulowana zamówienia w koszyku
    cumSum += quantity *products[choice][1] #cumSUM = cumSUM + (quantity *products[choice][1])
    #print("Twoj koszyk: ", basket)
    print("Twój koszyk: ")
    for element in basket:
        print ("| %8s | %8.2fzł | %5.1f |" %
              (element[0].center(10), element[1], element[2]))

    #print("Suma do zapłaty: ",cumSum, "ZŁ")
    print("Suma do zapłaty: %.2f zł" % cumSum)
