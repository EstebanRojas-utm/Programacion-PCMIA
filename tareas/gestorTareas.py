import datetime
class GestorTareas:
    def __init__(self):
        self.lista_tareas = []

    def anadir_tarea(self, tarea):
        self.lista_tareas.append(tarea)
        print(f"Tarea '{tarea.descripcion}' añadida.")

    def mostrar_tareas(self):
        if not self.lista_tareas:
            print("No hay tareas en la lista.")
            return

        print("--- Lista de Tareas ---")
        for i, tarea in enumerate(self.lista_tareas):
            print(f"Tarea #{i+1}")
            print(tarea.show_tarea())
            print("-" * 20)

    def completar_tarea(self, indice):
        if 0 <= indice < len(self.lista_tareas):
            tarea = self.lista_tareas[indice]
            tarea.set_estado(True)
            print(f"Tarea '{tarea.descripcion}' marcada como completada.")
        else:
            print("Índice de tarea no válido.")

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.lista_tareas):
            tarea_eliminada = self.lista_tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada.descripcion}' eliminada.")
        else:
            print("Índice de tarea no válido.")