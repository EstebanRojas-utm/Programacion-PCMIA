import datetime

class Library:
    def __init__(self) -> None:
        self.lista_libros = []

    def agregar_libro(self, libro):
        
        ban=0
        for i, lib in enumerate (self.lista_libros):
            if(lib.isbn == libro.isbn):
                print("El libro contiene el mismo ISBN")
                ban=1
                return

        if(ban == 0):
            self.lista_libros.append(libro)
            print(f"\nLibro '{libro.titulo}' añadido")


    def buscar_libro(self, libro):
        """ Esta funcion recibe el nombre del libro y verifica si esta disponible o no """

        ban = 0
        for i, lib in enumerate(self.lista_libros):

            if(libro == lib.titulo):
                ban = 1

        if(ban == 1):
            print(f"\nEl libro: {libro} esta disponible")
        else:
            print(f"\nEl libro: {libro} no esta disponible")    



    def libros_aPrestamo(self):
        if not self.lista_libros:
            print("No hay libros en la lista.")
            return        

        print("\n--- Lista de Libros disponibles para prestamo ---")
        for i, libro in enumerate(self.lista_libros):
            if (libro.disponible == True):
                print(f"Libro #{i+1}")
                print(libro.show_libro())
                print("-" * 20)     

    def prestar_libro(self, libro):
        if not self.lista_libros:
            print("No hay libros en la lista.")
            return
        print("\n---Verificando si el libro se puede prestar---")
        ban=0
        for i, lib in enumerate(self.lista_libros):
            if (lib.titulo == libro):
                if(lib.disponible == True):
                    print(f"El libro: {libro} esta disponible para prestamo")
                    lib.disponible = False
                    ban=1
                else:
                    print(f"El libro: {libro} no esta disponible para prestamo")
                    ban=1

        if(ban == 0):
            print(f"El libro {libro} no se encuentra en la bibleoteca") 

    def devolver_libro(self, libro):
        if not self.lista_libros:
            print("No hay libros en la lista.")
            return

        print("\n---Devolviendo libro---")
        ban=0
        for i, lib in enumerate(self.lista_libros):
            if (lib.titulo == libro):
                lib.disponible = True
                print(f"Libro devuelto {libro} \nGracias por su preferencia")
                ban=1

        if(ban == 0):
            print(f"El libro {libro} no es de la bibleoteca")                   
        
                    


