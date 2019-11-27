zdanie1 = False
zdanie2 = False
result00 = not (zdanie1 and zdanie2) == (not zdanie1) or (not zdanie2)

zdanie1 = False
zdanie2 = True
result01 = not (zdanie1 and zdanie2) == (not zdanie1) or (not zdanie2)

zdanie1 = True
zdanie2 = False
result10 = not (zdanie1 and zdanie2) == (not zdanie1) or (not zdanie2)

zdanie1 = True
zdanie2 = True
result11 = not (zdanie1 and zdanie2) == (not zdanie1) or (not zdanie2)

print("IS TAUTOLOGY?")
print (result00, result01, result10, result11)