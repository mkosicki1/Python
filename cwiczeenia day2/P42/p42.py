from random import sample
#  losuje bez zwracania z populacji - listy wartości
# określoną w argumencie metody liczbę razy

population = range(1,50)
quantity = 6
result = sample(population, quantity)
print(result)
result.sort()
print(result)
result.sort(reverse=False)
print(result)
result.sort(reverse=True)
print(result)
