from cw_day7.database_app.controller.TaskManagerController import TaskManagerController

start = TaskManagerController()
#start.insertUser("mk@mk.pl", "mk", "Miroslaw", "Kosicki", "M")
#start.insertUser("kk@mkk.pl", "mkk", "Michal", "Kruczkowski", "M")
# start.selectUsers()
#start.insertTaskToUser("programowanie", "programowanie w python", "nowe", "2020-01-01", 5)
start.selectTask()
# start.selectSummaryTask()
#start.insertTaskToUser("programowanie", "programowanie w python", "nowe", "2020-01-01", 13)
#start.insertUser("kk@kk.pl", "kk", "Karol", "Kuba", "M")
#start.updateTaskDateStop(2, "2020-06-06")
#start.deleteTaskById(3)
# start.insertSubtaskToTask("obiektowosc", "2020-02-02", "otwarte",2)
# start.insertSubtaskToTask("dziedziczenie", "2020-05-02", "otwarte",4)
start.selectSummaryTask()