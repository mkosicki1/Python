def nonDefinedParameters(*elements): #paramętr gwiazdka -> przyjmuje dowolną liczbe argumentow
    sum=0
    for elem in elements:
        sum += elem
    return sum/len(elements)

print(nonDefinedParameters(1))
print(nonDefinedParameters(5,4,6))
print(nonDefinedParameters(2,2,2,2))