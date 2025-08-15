class Tarea:
    def __init__(self, descripcion, prioridad=0, fecha_vencimiento=None):
        self.descripcion = descripcion
        self.estado = False
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento

    def show_tarea(self):
        estado_str = "Completada" if self.estado else "Pendiente"
        vencimiento_str = self.fecha_vencimiento.strftime("%Y-%m-%d") if self.fecha_vencimiento else "No especificada"
        return (f"Descripción: {self.descripcion}\n"
                f"Estado: {estado_str}\n"
                f"Prioridad: {self.prioridad}\n"
                f"Fecha de Vencimiento: {vencimiento_str}")

    def set_estado(self, estado):
        self.estado = estado

    def show_info(self):
        return f"Descripción: {self.descripcion} | Estado: {'Completada' if self.estado else 'Pendiente'}"    
