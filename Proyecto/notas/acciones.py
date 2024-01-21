import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"ok {usuario[1]}!! Vamos a crear una nueva nota..")
        
        titulo = input("Introduce el titulo de tu nota : ")
        descripcion = input("Introduce el contenido de tu nota :")
        
        nota = modelo.Nota(usuario[0],titulo,descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota : {nota.titulo}")
        else:
            print(f"No se ha guardado la nota, lo siento {usuario[1]}")

    def mostrar(self,usuario):
        print(f"\nVale {usuario[1]}!! Aqui tienes tus notas:")
        
        notas = modelo.Nota(usuario[0],"","")
        notas = notas.listar()

        ##primero para mostrar alos alumnos
        # print(notas)

        for nota in notas:
            print("\n******************************")
            print(nota[2])
            print(nota[3])
    
    def borrar(self,usuario):
        print(f"\n Ok {usuario[1]}!! Vamos a borrar notas")

        titulo = input("Introduce el titulo de la nota a borrar : " )

        nota = modelo.Nota(usuario[0],titulo,"")
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"\n Hemos borrado la nota:  {nota.titulo}")
        else:
            print(f" No hemos podido borrar la nota")
      