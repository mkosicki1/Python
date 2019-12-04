##cwiczenie P40

liczbaRzymska = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V"}
decNumber = input("Podaj liczbę całkowitą (1-5)")

if(decNumber.isdecimal()):
    decNumber = int(decNumber)

    if(decNumber >= 0 and decNumber <= 5):
        print(liczbaRzymska[decNumber])
    else:
        print("Liczba jest spoza zakresu 0-5")
else:
    print("Podałeś błędne dane")


    # 2 sposob

#liczbaRzymska = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V"}


#try:
#decNumber = float(input("Podaj liczbę całkowitą (1-5)"))

    #if (decNumber >= 0 and decNumber <= 5):
        #print(liczbaRzymska[decNumber])
    #else:
        #print("Liczba jest spoza zakresu 0-5")
#exept:
    #print


