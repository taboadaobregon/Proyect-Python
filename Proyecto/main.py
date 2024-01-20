
from usuarios import acciones


print("""
    ¿Que deseas Hacer?:
    -registrar 
    -login 
""")

hazEl = acciones.Acciones()


acciones = input("escribeme tu accion : ")


if acciones == "registrar":
    hazEl.registrar()
elif acciones == "login":
    hazEl.login()
else:
    hazEl.Sinosepuede()


