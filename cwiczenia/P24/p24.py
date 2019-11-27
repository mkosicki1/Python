a = False
b = False
c = True
result1 =  (not a) and (not b) and (not c)
result2 =  (not a) and (not b) and  (c)
result3 =  (not a) and (b) and (not c)
result4 =  (a) and (not b) and (not c)


result5 = result1 or result2 or result3 or result4
print(result5)
