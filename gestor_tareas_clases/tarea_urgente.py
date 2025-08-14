import datetime
from lista_tareas import Tarea


class TareaUrgente(Tarea):
    def __init__(self, descripcion, fecha_limite):
        # Llama al constructor de la clase padre (Tarea)
        super().__init__(descripcion, prioridad=2, fecha_vencimiento=fecha_limite)

    def recordatorio_urgente(self):
        print(f"🚨 ¡RECORDATORIO! La tarea '{self.descripcion}' es urgente y vence el {self.fecha_vencimiento.strftime('%Y-%m-%d')}.")
