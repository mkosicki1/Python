def geometricSeries (n, a1=1, q =2):
    cumSum = 0
    for i in range(0, n):
        cumSum += a1*pow(q,i)
    return cumSum


print(geometricSeries(4, a1 = 3, q = 2))
print(geometricSeries(4, a1 = 4, q = 2))
print(geometricSeries(4, a1 = 3, q = 3))

def geometricSeries (n, a1=1, q =2):
    cumSum = 0
    elements = []
    for i in range(0, n):
        cumSum += a1*pow(q,i)
        elements.append(a1*pow(q,i))
    return cumSum, elements


print(geometricSeries(4, a1 = 3, q = 2))
print(geometricSeries(4, a1 = 4, q = 2))
print(geometricSeries(4, a1 = 3, q = 3))
print(geometricSeries(4, a1 = 2, q = 3))
print(geometricSeries(4, a1 = 4, q = -5))
print(geometricSeries(4, a1 = 6, q = (1/2)))
print(geometricSeries(4, a1 = 8, q = 1))
