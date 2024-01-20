import usuarios.usuario as modelo 

class Acciones:
    def registrar(self):
        print("\nRegistrando usuario")
        nombre = input("escribeme tu nombre :")
        apellido = input("escribeme tu apellido :")
        email = input("escribemee tu email :")
        password = input("escribeme tu contraseña :")

        usuario = modelo.Usuario(nombre,apellido,email,password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print(f"Lo sentimos hubo un error en el proceso de registro")

    def login(self):
        print("\nIniciando sesión") 
        try:

            email = input("escribemee tu email :")
            password = input("escribeme tu contraseña :")

            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenid@ a la plataforma {login[1]}, te has registrado en el sistema {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(f"Login icorrecto | intentalo mas tarde")

    def Sinosepuede(self):
        print("\nNo se puede realizar la acción solicitada.")
    
    def proximasAcciones(self,usuario):
        print("""
        Acciones Disponibles:
            - Crear Nota (crear)
            - Mostrar tus notas (mostrar)
            - Eliminar nota (eliminar)
            - Salir (salir)
        """)

        accion = input("Que quieres hacer?:")

        if accion == "crear":
            print("Vamos a crear")
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            print("Vamos a mostrar")
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            print("Vamos a eliminar")
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"ok {usuario[1]} hasta pronto")
            exit()
        else:
            print("Escribe bien lo que desee !!!")
            self.proximasAcciones(usuario)
