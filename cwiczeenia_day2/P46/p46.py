lista = [4,5,3,2,1,6]
index = int(input("Która wartość wstawisz: " + str(lista))) -1


if(index >=0 and index < len(lista)):
    print("Twój wybór: ", lista[index])
else:
    print("out of range")


# czy dwa pierwsze elementy listy sa dodatnie
if(lista[0]  >0 and lista[1] > 0):
    print("dwa pierwsze elementy są dodatnie")
elif(lista[0] > 0 and lista[1]<=0):
    print("tylko pierwszy element jest dodatni")
elif(lista[0] <=0 and lista[1] >0):
    print("tylko drugi element jest dodatni")
else:
    print("oba elementy są ujemne")


#sprawdx czy wprowadzone lista jest parzysta

print("Wprowadzona wartość jest: ", "parzysta" if ((index +1)%2 == 0) else "nieparzysta")