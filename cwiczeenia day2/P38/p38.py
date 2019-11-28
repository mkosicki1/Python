expiredate = [(10,10,2019), (1,4,2020), (5,3,2020)]
print("Data ważności: " + str(expiredate[0][0]) + "-" + str(expiredate[0][1]) + "-" + str(expiredate[0][2]))
print("Data ważności: " + str(expiredate[1][0]) + "-" + str(expiredate[1][1]) + "-" + str(expiredate[1][2]))
print("Data ważności: " + str(expiredate[2][0]) + "-" + str(expiredate[2][1]) + "-" + str(expiredate[2][2]))


expiredate = [(10,10,2019), (1,4,2020), (5,3,2020)]
while(True):
    inputDate = input("Wprowadz date w formacie dd-mm-yyyy lub Q -wyjdz: " )
    if(inputDate.upper()[0]) == "Q":
        break

        expiredate.append(tuple(inputDate.split("-")))

print(expiredate)