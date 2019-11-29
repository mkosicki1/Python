## pętla for in

lvls = ["A1", "A2", "B1", "B2", "C1", "C2"]

for lvl in lvls:
    print(lvl)


for i, lvl in enumerate(lvls):
    print(i, lvl)


# iterowanie po slownikach w for in

lvls = ["A1", "A2", "B1", "B2", "C1", "C2"]
lvlsNames = {lvls[0]: "Basic",
             lvls[1]: "Basic",
             lvls[2]: "Independent",
             lvls[3]: "Independent",
             lvls[4]: "Proficient",
             lvls[5]: "Proficient",
             }

for key in lvlsNames.keys():
    print(key, lvlsNames[key])

#for value in lvlsNames.values():
    #print(value)

slowo = "Mirek"

for i in slowo:
    print(i)