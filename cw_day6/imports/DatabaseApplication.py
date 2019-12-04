# importy sa adresowane od katalogu domowego -> nazwa projektu
#nazwa modulu wystepuje bez rozszerzenia
# alias zastepuje wszystko co jest w adresie modułu razem z jego nazwa
import cw_day6.imports.SecretVariables as sv
import random as rnd


# for i in dir(sv):
#     print(i)
# help(sv)

# for i in dir(rnd):
#     print(i)
# help(rnd)


# dostep do zmiennych
# print(sv.database)
# print(sv.username)
# print(sv.password)
# print(sv.host)
# print(sv.port)
#
# #dostep do metod
# print(sv.getConnection())
#
# # dostep do klas
#
# obiektKlasyZaimportowanej = sv.Hello("Michał")
# print(obiektKlasyZaimportowanej.name)
# print(obiektKlasyZaimportowanej)



import os
print("Direct ref", os.getcwd())

print("W katalogu, w którym sie znajdujemy aktualnie")
for i in os.listdir("."):
    print(i)

print("W katalogu pracowników jest coś takiego")
for i in os.listdir("C:\\Users\PC\\PycharmProjects"):
     print(i)