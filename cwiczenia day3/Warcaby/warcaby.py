kik = [
            ["_", "_", "_"],
            ["_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"]

      ]

print(kik)
print("lista zewnetrzna",len(kik))
print("pierwszy wiersz", len(kik[0]))
print("drugi wiersz", len(kik[1]))
print("trzeci wiersz", len(kik[2]))
kik[2][3]= "X"
print(kik)
kik [1][1:3] = ["O", "O"]
print(kik)


kik.append(["*", "*", "*"])
print(kik)

kik.insert(0,["*", "*", "*"])
print(kik)
print(len(kik))
kik = [["^", "^", "^"]] + kik
print(kik)