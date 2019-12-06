import cw_day7.sql.database_credentials as secret
import pymysql

from cw_day7.database_app.model.Subtask import SubTask
from cw_day7.database_app.model.Task import Task
from cw_day7.database_app.model.User import User


def toExport():
    connection = pymysql.connect(
        host=secret.host,
        user=secret.username,
        password=secret.password,
        db=secret.database_name,
        charset='utf8',
        port=3305
    )
    print("...CONNECTED...")
    cursor = connection.cursor()
    return connection, cursor


class TaskManagerController:

    def __init__(self):
        db = toExport()
        self.connection = db[0]
        self.cursor = db[1]



    def insertUser(self, email, password, name, lastname, gender):
        u = User(email, password, name, lastname, gender)

        #wykonanie polecenia SQL - nie zwraca wyniku
        self.cursor.execute("INSERT INTO user VALUES (default, %s, %s, %s, %s, %s)",
                            (u.email, u.password, u.name, u.lastname, u.gender))

        self.connection.commit()
        print("Dodano", u.email)
        decision = input("Czy na pewno chcesz dodać: " + u.email + "(T/N)").upper()
        # if(decision == "T"):
        #     self.connection.commit() ### potwierdzenie transakcji
        #     print("Dodano", u.email)
        # else:
        #     self.connection.rollback() #- odrzucenie transkacji
        #     print("Nie dodano", u.email)
    def selectUsers(self):
        # wykonanie zapytania SQL - ZWRACA WYNIK
        self.cursor.execute("SELECT * FROM user")
        result = self.cursor.fetchall() # pobieramy wszystkie wyniki
        for row in result:
            u = User(row[1], row[2], row[3], row[4], row[5], row[0])
            print(u)

    def insertTaskToUser(self, name, description, status, date_stop, user_id):
        t = Task(name, description, status, date_stop, user_id)
        self.cursor.execute(
            "INSERT INTO task VALUES (default, %s, %s, %s, default, %s, %s)",
            (t.name, t.description, t.status, t.date_stop, t.user_id))
        self.connection.commit()
        print("Dodano zadanie: ", t.name)
    def selectTask(self):
        self.cursor.execute("SELECT*FROM task")
        for row in self.cursor.fetchall():
            t = Task(row[1], row[2], row[3], row[5], row[6], row[0], row[4] )
            print(t)

    def selectSummaryTask(self):
        self.cursor.execute("SELECT *FROM summary")
        print("| %20s | %20s | %20s | %20s | %20s | %20s | %20s |" %
                  ("ZADANIE", "OPIS", "PODZADANIE", "DEADLINE", "STATUS", "IMIE", "NAZWISKO"))
        for row in self.cursor.fetchall():
            print("| %20s | %20s | %20s | %20s | %20s | %20s | %20s |" %
                  (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))


    def updateTaskDateStop(self, task_id, newdeadline):
        self.cursor.execute("UPDATE task SET date_stop = %s WHERE task_id = %s", (newdeadline, task_id))
        self.connection.commit()
        self.selectTask()

    def deleteTaskById(self, task_id):
        self.cursor.execute("DELETE FROM task WHERE task_id = %s", task_id)
        self.connection.commit()
        print("Usunięto zadanie:", task_id)
        self.selectTask()

    def insertSubtaskToTask(self, detail_description, deadline, status, task_id):
        st = SubTask(detail_description, deadline, status, task_id)
        self.cursor.execute(
        "INSERT INTO SubTask VALUES (default, %s, %s, %s, %s)",
            ( st.detail_description, st.deadline, st.status, st.task_id))
        self.connection.commit()
        print("Dodano podzadanie: ", st.detail_description)