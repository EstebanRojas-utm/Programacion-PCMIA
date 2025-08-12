import datetime
from lista_tareas import Tarea

#Crear una tarea con fecha de vencimiento
tarea1 = Tarea(
    descripcion="Ecuaciones diferenciales de terecer orden",
    prioridad=1,
    fecha_vencimiento=datetime.date(2025, 8, 22)
)

#Crear una tarea sin fecha de vencimiento
tarea2= Tarea(
    descripcion="Investigar las CNN´s ",
    prioridad=0
)


# Mostrar las tareas
print("\n--- Mostrando tareas iniciales ---")
tarea1.show_tarea()
tarea2.show_tarea()

#Cambiar el estado de una tarea
print("\n--- Actualizando el estado de una tarea ---")
tarea1.set_estado(True)

#Mostrar tarea actualizada
print("\n--- Mostrando tarea actualizada ---")
tarea1.show_tarea()
tarea2.show_tarea()
