import datetime

class Tarea:

    def __init__(self, descripcion, prioridad=0, fecha_vencimiento=None ) :
        self.descripcion = descripcion
        self.estado = False
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento

    def show_tarea(self):
        """
        Muestra los detalles de la tarea.
        """
        estado_str = "Completada" if self.estado else "Pendiente"
        vencimiento_str = self.fecha_vencimiento.strftime("%Y-%m-%d") if self.fecha_vencimiento else "No especificada"
        print(f"--- Detalles de la Tarea ---")
        print(f"Descripción: {self.descripcion}")
        print(f"Estado: {estado_str}")
        print(f"Prioridad: {self.prioridad}")
        print(f"Fecha de Vencimiento: {vencimiento_str}")
        print(f"----------------------------")

    def set_estado(self, estado):
        """
        Cambia el estado de la tarea.

        Args:
            estado (bool): El nuevo estado de la tarea (True para completada, False para pendiente).
        """
        self.estado = estado
        estado_str = "completada" if self.estado else "pendiente"
        print(f"El estado de la tarea '{self.descripcion}' ha sido cambiado a '{estado_str}'.")
    






        