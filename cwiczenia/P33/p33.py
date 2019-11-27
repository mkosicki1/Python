#v = SPK*(1+ p /m)**(n*m)

SPK = float(input("podaj SPK: "))
p = int(input("Podaj procent: "))/100
n = int(input("Podaj okres trwania lokaty: "))
m = int(input("Podaj ilość okresów kapitalizacji: "))

print("Stan konta w przyszłości: ",
      round(SPK *(1 + (p/m))** (n*m),2))

