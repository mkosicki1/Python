# baza danych
productNames = "Chleb", "Mleko", "Cuksy"
productPrices = 1.99, 2.50, 12.99
productquantity = "szt.", "l", "kg"

# zamówienie

productOrder =  2,0.5, 0.3


# prezentacja zamówienia

print(productNames[0], productOrder[0], productquantity[0], sep = "\t\t")
print(productNames[1], productOrder[1], productquantity[1], sep = "\t\t")
print(productNames[2], productOrder[2], productquantity[2], sep = "\t\t")

## kwota do zapłaty

print("SUMA",round(productPrices[0]*productOrder[0] +
                   productPrices[1]*productOrder[1] +
                   productPrices[2]*productOrder[2],2) ,"zł", sep = "\t\t")





