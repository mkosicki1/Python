#  import z okreslonej lokalizacji konkretnych składowych
# składowe sa dostepne bez adresowania
# składowe sa importowane tylko po nazwach
from cw_day6.imports.SecretVariables import Hello
from cw_day6.imports.SecretVariables import database, username, password
from cw_day6.imports.SecretVariables import getConnection

print(username)
print(password)
print(database)

#print(port) - nie jest importowany

print(getConnection())

h = Hello("MK")
print(h)

# CTRL +ALT + O - optimize imports