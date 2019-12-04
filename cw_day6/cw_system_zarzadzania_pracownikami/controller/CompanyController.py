import hashlib

from cw_day6.cw_system_zarzadzania_pracownikami.model.Trainee import Trainee
from cw_day6.cw_system_zarzadzania_pracownikami.model.employee import Employee, Permission


class CompanyController:
    employees = [
        Employee("mk1", "mk1", "PYTHON DEV", 11000, Permission.ROLE_EMPL),
        Employee("mk2", "mk2", "JAVA DEV", 9000, Permission.ROLE_EMPL),
        Employee("mk3", "mk3", "PYTHON DEV", 12000, Permission.ROLE_EMPL),
        Employee("mk4", "mk4", "MANAGER", 14000, Permission.ROLE_MAN),
        Employee("mk5", "mk5", "SCRUM MASTER", 13000, Permission.ROLE_MAN),
        Employee("mk6", "mk6", "HEAD", 17000, Permission.ROLE_HEAD),
        Employee("mk7", "mk7", "HEAD", 21000, Permission.ROLE_HEAD),
        Employee("mk8", "mk8", "DEV OPS", 11500, Permission.ROLE_EMPL),
        Trainee("t1", "t1"),
        Trainee("t2", "t2"),
        Trainee("t3", "t3")
    ]

    #1. dodawanie pracownika lub praktykanta z unikatowym loginem

    def addEmployeeOrTr(self, o):
        if(o.__class__.__name__ == "Trainee" or o.__class__.__name__ == "Employee"):
            if(self.loginValid(o.login)):
                print("Dodano pracownika: ",o.login, o.position)
                self.employees.append(o)
            else:
                print("Istnieje już taki login w naszej bazie danych")
        else:
            print("Dany obiekt nie jest pracownikiem anie praktykantem")

    #1* sprawdzenie czy dany login nie istnieje w liscie employee

    def loginValid(self, login):
        for e in self.employees:
            if(e.login == login):
                return False
        return True


    #2. wyświetlenie wszystkich pracowników i praktykantów posortowanych po pensji DESC
    def getEmployees(self):
        #sortowanie po pensji
        for e in sorted (self.employees, key=lambda e : e.salary, reverse=True):
            print(e)

    #3.  wyświetlenie tylko kierowników lub dyrektorów posortowanych po loginie A-Z
    def getManagersAndHeadsOrderByLoginASC(self):
       #1sposob
       result = filter(lambda e: e.__class__.__name__ == "Employee" and e.permission.value in [2, 3],
                       self.employees)
       for i in sorted(result, key=lambda e: e.login, reverse=False):
           print(i)

       #2 sposob
        # for e in self.employees:
        #     if(e.__class__.__name__ == "Employee"):
        #         if(e.permission.value in [2,3]):
        #             print(e)



    #4.  wyświetlenie praktykantów po loginie Z-A
    def getTraineeOrderByLogin(self):
        # filter - filtruje liste pracowników i zwrcaa tylko praktykantów
        result = filter(lambda e : e.__class__.__name__ == "Trainee", self.employees)
        for t in sorted(result, key=lambda t : t.login , reverse=True):
            print(t)

    #5.  przypisywanie nagrody do pracownika lub praktykantow po loginie, jeśli nie podamy loginu to premia dla wszystkich
    def getPrise(self, amout, login=""):
        if(login != ""):
            isLogin = False
            #wyszukaj pracownika
            for e in self.employees:
                if(e.login == login):
                        e.assignPrise(amout)
                        isLogin = True
                        break
            if(isLogin == False):
                print("Błędny login pracownika")
        else:
                for e in self.employees:
                    e.assignPrise(amout)
        self.getEmployees()



    #6.  zmiana pensji tylko dla pracownika

    def ChangeEmployeeSalary(self, login, salary):
        isEmployee = False
        for e in self.employees:
            if(e.login == login and e.__class__.__name__== "Employee"):
                e.salary = salary
                isEmployee = True
                break
        if(isEmployee == False):
            print("Błedny login lub typ pracownika")

        self.getEmployees()

    #7. usuwanie pracownika lub praktykanta z listy

    # 1 sposob
    def DelEmployeeOrTrainee(self,login):
        isFound = False
        for e in self.employees:
            if(e.login == login):
                self.employees.remove(e)
                print("Usunięto: ", e.login)
        if(isFound == False):
            print("Nie ma takiego pracownika")

        # 2 sposob = z potwierdzeniem hasła
    def DelEmployeeOrTraineeWithConfirm(self, login):
            isFound = False
            for e in self.employees:
                if(e.login == login):
                    isFound = True
                    inputPassword = input("Potwierdź usuwanie hasłem").strip(" ")
                    if (e.password == hashlib.md5(
                            ("salt:XYZ"+inputPassword).encode('utf-8')).hexdigest()):

                        self.employees.remove(e)
                        print("Usunięto: ", e.login)
                    else:
                        print("Błąd potwierdzenia")
            if (isFound == False):
                print("Nie ma takiego pracownika")
            self.getEmployees()

