#panel logowania

logs = {"user" : "user", "admin" : "admin"}
login = input("Podaj login: ")
password = input("Podaj hasło" )



if(login not in logs.keys()): #błedny login
    print("błędny login")
elif(logs[login] == password): # poprawne logowanie
    print("zalogoowano")
else:
    print("błędne hasło") # błędne hasło
