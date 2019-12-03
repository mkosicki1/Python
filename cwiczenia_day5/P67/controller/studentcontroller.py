# kontroller - klasa obslugi zadan uzytkownika pochodzacy
# z widoku (html, cli, window)
# implementuje logike aplikacji
import datetime

from cwiczenia_day5.P67.models.Student import Student


class StudentController:
    students = []
    # konstruktor - pobranie i aktualizacja listy studentów z pliku
    def __init__(self):
        inputFile = open("database.csv", "r") #otwarcie pliku do odczytu
        #print(inputFile.read())
        for index, line in enumerate(inputFile.readlines()):
            if(index == 0):
                print(line) # wypializacji aktuesujemy dat
                continue
            # każda linijkę z pliku mapujemy na obiekt student
            rowData = line.split(";")
            #czyszczenie napisu zawierajacego oceny z {[] ,}
            grades = rowData[3].replace("[", "").replace("]", "").split(", ")
            # konwersja ocen na float
            try:
                for index, grade in enumerate(grades):
                    grades[index] = float(grade)
            except:
                grades = []

            # utworzenie obiektu studenta na podstawie danych z jednej linii pliku
            s=Student(rowData[0], rowData[1], rowData[2], grades)



            #zapis zmapowanego obiektu do listy students
            self.students.append(s)
        inputFile.close() # zamknięcie strumienia danych do pliku

    # metoda dodajaca studenta do listy
    def addStudent(self, index, name, lastname):
        if(self.validdateStudentIndex(index)): # wywołanie walidacji
            #utworzenie obiektu studenta - odwolanie do modelu
            s= Student(index, name, lastname)
            self.students.append(s)
            print("Dodano: ", s)
        else:
            print("Istnieje student o wskazanym indeksie")
    # metoda do walidacji danych studenta
    def validdateStudentIndex(self, inputIndex):
        for student in self.students:
            if(student.index == inputIndex):
                # jezeli juz wystepuje taki index
                return False # nie dodajemy do listy
        return True # dodajemy do listy
    # metoda dodajaca ocene
    def addGradeToStudent(self, inputIndex, grade):
        gradesTemplate = [2,3,3.5,4,4.5,5,5.5]
        if(grade in gradesTemplate):
            isAdded = False
            for student in self.students:
                if (student.index == inputIndex):
                    isAdded = True
                    student.addGrade(grade)
                    print("Dodano ocenę")
                # wypisz zaktualizowana liste studentow
            if(isAdded == False):
                print("NIe ma studenta o takim indeksie")
            self.getStudents()
        else:
            print("Podałeś niepoprawną ocenę")

            # metoda do usuwania studenta po indeksie
    def deleteStudentByIndex(self, inputIndex):
        for student in self.students:
            if (student.index == inputIndex):
                        print("Usunięto", student)
                        self.students.remove(student)
        self.getStudents()

    # metoda wypisujaca wszystkich studentow z listy studentow

    def getStudents(self):
        print("| %6s | %15s | %15s | %20s | %7s |"
              % ("INDEKS", "IMIĘ", "NAZWISKO", "OCENY", "ŚREDNIA"))
        for student in self.students:
            print(student)

    def __del__(self): # desktruktor wywołuje się automatycznie gdy niszczony jest obiekt z pp
        outputFile = open("database.csv", "w")
        outputFile.write("data aktualizacji: " + str(datetime.datetime.now()) +"\n")
        for student in self.students:
            outputFile.write(student.index+";"+student.name+";"+student.lastname+";"+str(student.grades)+";"+str(student.calculateAVG())+"\n")
        # zamknięcie strumienia danych
        outputFile.close()


# testowanie kontrolera
#sc = StudentController()
#sc.addStudent(123123, "test", "test")
#sc.addStudent(123122, "test1", "test1")
#sc.getStudents()
#sc.addGradeToStudent(123123,4)
#sc.addGradeToStudent(123123,3)
#sc.addGradeToStudent(123121,3) # BŁĄD DANYCH
#sc.addGradeToStudent(123123,33)# BŁAD DANYCH