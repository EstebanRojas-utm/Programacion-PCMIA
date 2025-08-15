import datetime
from book import Book
from library import Library

if __name__ == "__main__" :
    gestor = Library()

    #instancias de tipo Books
    libro1 = Book("Ecuaciones diferenciales", "Albert Einstein", datetime.date(1980, 8, 12), 14525)
    libro2 = Book("Don Quijote de la mancha", "Cervantes", datetime.date(1977, 6, 21), 78954)
    libro3 = Book("Algebra lineal", "maxwell", datetime.date(1970, 8, 12), 14525)

    #Agregar libros
    gestor.agregar_libro(libro1)
    gestor.agregar_libro(libro2)
    gestor.agregar_libro(libro3)


    #Libros a prestamos
    gestor.libros_aPrestamo()
    
    #Buscar libros disponibles por titulo
    gestor.buscar_libro("Don Quijote de la mancha")
    gestor.buscar_libro("Diario de anafrank")

    #verificar si un libro se puede prestar 
    gestor.prestar_libro("Ecuaciones diferencial")
    gestor.prestar_libro("Ecuaciones diferenciales")
    gestor.prestar_libro("Ecuaciones diferenciales")

    #Libros a prestamos
    gestor.libros_aPrestamo()

    #Regresar un libro
    gestor.devolver_libro("Ecuaciones diferenciales")

    #Libros a prestamos
    gestor.libros_aPrestamo()
