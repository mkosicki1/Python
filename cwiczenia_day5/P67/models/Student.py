# KLASA MODELU DETERMINUJE STRUKTURE DANYCH
# WSPIERA PODEJSCIE ORM = OBJECT RELATIONSHIP MAPPING
#RZUTUJE CECHY DANYCH POCHODZACE Z TABELKI SQL NA OBIEKT PYTHON

class Student:
    # konstruktor klasy
    def __init__(self, index, name, lastname, grades = []):
        self.index = index
        self.name = name
        self.lastname = lastname
        self.grades = grades
    # metoda dodawania ocen do listy grades
    def addGrade(self, grade):
        self.grades.append(grade)
    #metoda zwracajaca średnia ocen studenta
    def calculateAVG(self):
        cumSum = 0
        if(len(self.grades) == 0):
            return 0
        for grade in self.grades:
            cumSum += grade

        return cumSum/len(self.grades)

    def __str__(self):
        return "| %6s | %15s| %15s | %20s | %7s |" % \
                        (self.index, self.name, self.lastname, self.grades,
                         "B/D" if self.calculateAVG() == 0 else round(self.calculateAVG(),2))


# testowanie modelu
# s = Student(123123, "test", "test")
# s.addGrade(5)
# s.addGrade(3)
# s.addGrade(2)
# print(s)