# funkcja odwołujaca sie do obiektu globalnie zadeklarowanego w skrypcie
def returnColour():
    global value # pobieram wartosc globalna
    value = not value # modyfikacja obiektu globalnego


    return value;
value = True
print(returnColour())
print(returnColour())
print(returnColour())
print(returnColour())

def returnColour():
    global value # pobieram wartosc globalna
    value = not value # modyfikacja obiektu globalnego


    return "black" if value else "white";
value = True
print(returnColour())
print(returnColour())
print(returnColour())
print(returnColour())