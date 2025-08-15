from task import Tarea

# Tarea con fecha de vencimiento (polimorfismo en show_info)
class TaskDate(Tarea):
    def __init__(self, descripcion, fecha_vencimiento):
        super().__init__(descripcion)
        self.fecha_vencimiento = fecha_vencimiento

    def show_info(self):
        base_info = super().show_info()
        return f"{base_info} | Fecha Vencimiento: {self.fecha_vencimiento.strftime('%Y-%m-%d')}"
