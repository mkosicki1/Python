#### definicja metody

def CEL_FAR(CEL):
    return 32 + (9* CEL)/5


# Wywołanie metody/funkcji
print("| %5s | %6s |" % ("C", "F"))
for CEL in range(40,-25,-5):
    if(CEL == 0):
        print("| %+5i | %6.1f |" % (CEL, CEL_FAR(CEL)))
    print("| %+5i | %6.1f |" % (CEL, CEL_FAR(CEL)))


##definicja

def temperatureTable(start, stop, step):
    print("| %5s | %6s |" % ("C", "F"))

    for CEL in range(stop, start - step, -step):
        if (CEL == 0):
            print("| %+5i | %6.1f |" % (CEL, CEL_FAR(CEL)))
        else:
            print("| %+5i | %6.1f |" % (CEL, CEL_FAR(CEL)))

temperatureTable(-100,-50,10)
temperatureTable(-5,45,5)