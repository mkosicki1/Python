def isGrade(grade):
    return grade in gradesTemplate
def gradesAVG(grades):
    sum = 0
    for grade in grades:
        sum += grade
    return sum/len(grades)


gradesTemplate = (3.0, 3.5,4.0,4.5,5.0)
grades = []


while(True):
    grade = input("Podaj ocenę:(ENTER - wyjście) ")
    if(grade == ""):
            print("Średnia ocen: %.2f" % gradesAVG(grades))
            break
    try:
        grade = float(grade)
    except:
        print("Ocena musi być liczbą!!!")
    # sprawdzenie  czy wartość liczbowa jest na skali ocen
    if(not isGrade(grade)):
        print("Nie ma takiej oceny w skali ocen!")
        continue
    grades.append(grade)
    print("Wprowadzone oceny: %s" % grades)


