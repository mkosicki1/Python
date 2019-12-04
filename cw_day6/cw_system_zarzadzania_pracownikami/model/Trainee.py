import hashlib
class Trainee:
    def __init__(self, login, password):
        self.login = login
        #self.password = hashlib.md5(password.encode('utf-8')).digest()
        self.password = hashlib.md5(("salt:XYZ"+password).encode('utf-8')).hexdigest()# 0-9abcdef
        self.position = "PRAKTYKANT"
        self.salary = 0
    def assignPrise(self, amount):
        self.salary += amount
    def __str__(self):
        return "| %15s | %10s |%15s | %13.2f zł |" % \
                (self.login, self.password[0:8], self.position, self.salary)
                #(self.login,10*"*", self.position, self.salary)

#test
#t = Trainee("MichałK", "qwe123")
#t.assignPrise(-1000)
#print(t)
