
for x in range(1,11):
    for y in range (1,11):
        print("%3i" % (x*y), end= " ")
    print()

x = range(1,11)
for i in x:
    for j in x:
        print("%3i" % (i*j), end= " ")
    print()

x = range(1,11) # system dziesietny
for i in x:
    for j in x:
        print("%3x" % (i*j), end= " ")
    print()

for x in range(5, 100, 10):
        print("%4i%6i%8i" % (x, x ** 2, x ** 3))


for x in range(5,100,10):
    print("Pierwiastkiem liczby %2i jest %5.3f" % (x,x**0.5))


# system binarny
x = range(1,11) # system dziesietny
for i in x:
    for j in x:
        print("%10s" % bin(i*j)[2:].zfill(10), end= " ")
    print()