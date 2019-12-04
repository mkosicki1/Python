from cw_day6.cw_system_zarzadzania_pracownikami.controller.CompanyController import CompanyController
from cw_day6.cw_system_zarzadzania_pracownikami.model.Trainee import Trainee
from cw_day6.cw_system_zarzadzania_pracownikami.model.employee import Employee

cc = CompanyController()
cc.addEmployeeOrTr(Employee("e1","e2","Junior DEV", 5000))
cc.addEmployeeOrTr(Employee("e1","e2","Junior DEV", 5000))
cc.addEmployeeOrTr("Pani Jadzia z gazowni")
cc.addEmployeeOrTr(Trainee("p1","p1"))
cc.getEmployees()
#cc.getTraineeOrderByLogin()
#cc.getManagersAndHeadsOrderByLoginASC()
# cc.getPrise(1000,"p1")
# cc.getPrise(1000,"e11")
#print()
# cc.ChangeEmployeeSalary("mk1", 1000)
# cc.ChangeEmployeeSalary("mk1", 11000)
cc.DelEmployeeOrTraineeWithConfirm("mk9")