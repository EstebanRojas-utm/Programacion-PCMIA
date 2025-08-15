from task import Tarea

# Tarea recurrente (polimorfismo en show_info)
class TaskRecurrent(Tarea):
    def __init__(self, descripcion, periodo_dias):
        super().__init__(descripcion)
        self.periodo_dias = periodo_dias

    def show_info(self):
        base_info = super().show_info()
        return f"{base_info} | Recurrencia: Cada {self.periodo_dias} días"