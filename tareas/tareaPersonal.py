from task import Tarea

class TareaPersonal(Tarea):
    def __init__(self, descripcion):
        # Llama al constructor de la clase padre con valores predeterminados
        super().__init__(descripcion, prioridad=1)
