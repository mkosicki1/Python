## dana jest lista wartości

a = [.3, .4, 3.2, .3, 1, 5.4, 2, 1, 17, 7]
# napisz program filtrujacy wartosci po zadanym przez uzytkownika progu
#tj. w tablicy wynikowejpojawiaja sie tylko wartosci większe od treshold

treshold = float(input("Podaj próg odcięcia: "))
result = []
index = 0
print(treshold)
while(index < len(a)):
        if(a[index] > treshold):
            result.append(a[index])
        index +=1

print(result)

###

# napisz program filtrujacy wartosci po zadanym przez uzytkownika progu
#tj. w tablicy wynikowejpojawiaja sie tylko wartosci większe od treshold
# prog dolny i górny
tresholdLow = float(input("Podaj próg odcięcia dolny: "))
tresholdTop = float(input("Podaj próg odcięcia gorny: "))
result = []
index = 0


while(index < len(a)):
        if(a[index] > tresholdLow and a[index] < tresholdTop):
            result.append(a[index])
        index +=1

print(result)


#####

tresholdLow = float(input("Podaj próg odcięcia dolny: "))
tresholdTop = float(input("Podaj próg odcięcia gorny: "))
categorizedResult = []
index = 0


while(index < len(a)):
        if(a[index] > tresholdLow and a[index] < tresholdTop):
            categorizedResult.append(1)
        else:
            categorizedResult.append(0)

        print(a[index], categorizedResult[index])
        index += 1


print(a)
print(categorizedResult)


tresholdLow = float(input("Podaj próg odcięcia dolny: "))
tresholdTop = float(input("Podaj próg odcięcia gorny: "))
categorizedResult = []
index = 0
class0 = [] # lista przechowujaca wartosci sklasyfikowane 0
class1 = [] # lista przechowujaca wartosci sklasyfikowane 1
labelsDist = {0 : class0, 1 : class1}
while(index < len(a)):
        if(a[index] > tresholdLow and a[index] < tresholdTop):
            categorizedResult.append(1)
            class1.append(a[index])
        else:
            categorizedResult.append(0)
            class0.append(a[index])

        print(a[index], categorizedResult[index])
        index += 1


print(a)
print(categorizedResult)
print(labelsDist)
#print(labelsDist[0])
#print(labelsDist[1])


## pętla for in

lvls = ["A1", "A2", "B1", "B2", "C1", "C2"]

for lvl in lvls:
    print(lvl)