
class Book:
    def __init__(self, titulo, autor, fecha_publicacion, isbn) -> None:
        self.titulo = titulo
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion
        self.isbn = isbn
        self.disponible = True

    def set_disponible(self, disponible):
        self.disponible = disponible

    def show_libro(self):
        disponible_str = "Disponible" if self.disponible else "No disponible" 

        return(f"Titulo: {self.titulo}\n"
               f"Autor: {self.autor}\n"
               f"fecha de publicacion: {self.fecha_publicacion}\n"
               f"ISBN {self.isbn} \n" )    

        

