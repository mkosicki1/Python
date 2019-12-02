# n! = n*(n-1)*(n-2)


def silnia(n):
    result = 1
    while (n>1):
        result *= n # result = result *n
        n -= 1      # n= n-1

    return result

n = 5
print("%d!=%d" %(n, silnia(n)))


def silniaRec(n): # REKURENCJA
    if(n == 2):
        return n
    return n * silnia(n -1);


n = 5
print("%d!=%d" %(n, silnia(n)))
print("%d!=%d" %(n, silniaRec(n)))