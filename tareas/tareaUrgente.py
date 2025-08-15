from task import Tarea

class TareaUrgente(Tarea):
    def __init__(self, descripcion, fecha_limite):
        # Llama al constructor de la clase padre
        super().__init__(descripcion, prioridad=3, fecha_vencimiento=fecha_limite)

    def recordatorio_urgente(self):
        print(f"🚨 ¡RECORDATORIO! Esta tarea es URGENTE: '{self.descripcion}' y vence el {self.fecha_vencimiento.strftime('%Y-%m-%d')}.")
