from cw_day6.cw_system_zarzadzania_pracownikami.model.Trainee import Trainee

from enum import Enum


# typ wyliczeniowy - dopuszcza tylko wybrane możliwości
class Permission(Enum):
    ROLE_EMPL = 1
    ROLE_MAN = 2
    ROLE_HEAD = 3


class Employee(Trainee):
        def __init__(self, login, password, position, salary, permission=Permission.ROLE_EMPL):
            super().__init__(login, password)
            self.position = position
            self.salary = salary
            self.permission = permission
        def __str__(self):
            return super().__str__() + " %5s |" % (self.permission.value)

# e = Employee("mk", "mk", "Python Dev", 10000)
# e1 = Employee("mk1", "mk1", "Python Dev", 11000, Permission.Role_Man)
# e.assignPrise(5000)
# print(e)
# print(e1)
# t = Trainee("X", "Z")
# print(t)