import re # regular expresions

import os

pattern1 = re.compile("^[d]") # zaczyna sie od d
print(pattern1.match("dog"))

pattern1 = re.compile("^[dD].*[gG]$") # ZACZYNA SIE NA d LUB D I KONCZY g LUB G
print(pattern1.match("doog"))
print(pattern1.match("DoG"))
print(pattern1.match("gdog"))

pattern1 = re.compile("^[dD].{1,3}[gG]$")
print(pattern1.match("dooog"))
print(pattern1.match("DoG"))
print(pattern1.match("gdog"))
print(pattern1.match("ddog"))


pattern1 = re.compile("^[dD].{1,}[gG]$")
print(pattern1.match("dooog"))

postalCode =input("poda kod pocztowy")
#postalCode = "02-409"
result = re.search("[0-9]{2}-[0-9]{3}", postalCode)
result = re.search("[0-9]{2}\s-\s[0-9]{3}", postalCode)# spacja przed - i po -

if(result is None):
    print("Błąd kodu pocztowego")
else:
    print("Jest ok")

#.{1,}[\.]{1}pdf$
#.*[\.]{1}pdf$

import time

filepattern = re.compile(".{1,}[\.]{1}(pdf|ppt|pptx|exe)$")
path = "C:\\Users\\PC\\Desktop"
path1 = "E:\KURSY\Reaktor PWN Analityk danych"
#os.chdir(path)
os.chdir(path1)# change directory
#os.mkdir("test") # utworzenie katalogu
for file in os.listdir('.'): # list directory w aktualnej lokalizacji
    if(re.search(filepattern, file)):
        #print(file)
        print("%-50s | %10.2f MB | %20s | %20s |"
              % (file, os.path.getsize(file)/(10**6),
                 time.ctime(os.path.getctime(file)),
                 time.ctime(os.path.getmtime(file))))

regex = "^\w[^\.]\w$"






