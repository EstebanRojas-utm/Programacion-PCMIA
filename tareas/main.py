import datetime 
from gestorTareas import GestorTareas
from task import Tarea
from tareaPersonal import TareaPersonal
from tareaUrgente import TareaUrgente
from simpleTask import SimpleTask
from TaskDate import TaskDate
from taskRecurrent import TaskRecurrent

# Main que demuestra el polimorfismo
if __name__ == "__main__":
    lista_tareas = [
        SimpleTask("Ir de compras"),
        TaskDate("Ecuaciones diferenciales", datetime.date(2025, 8, 22)),
        TaskRecurrent("Pagar el alquiler", 30)
    ]

    print("--- Demostración de Polimorfismo ---")
    for tarea in lista_tareas:
        print(f"Tipo de objeto: {type(tarea).__name__}")
        print(tarea.show_info())
        print("-" * 20)




"""
# Uso de la herencia
if __name__ == "__main__":
    tareas = [
        Tarea("Ecuaciones diferenciales", 1, datetime.date(2025, 8, 22)),
        TareaUrgente("Preparar presentación del proyecto", datetime.date(2025, 8, 18)),
        TareaPersonal("Comprar alimentos para la semana")
    ]

    print("--- Mostrando todas las tareas ---")
    for tarea in tareas:
        print(tarea.show_tarea())
        if isinstance(tarea, TareaUrgente):
            tarea.recordatorio_urgente()
        print("-" * 20)
"""


"""if __name__ == "__main__":
    gestor = GestorTareas()

    tarea1 = Tarea("Ecuaciones diferenciales de tercer orden", 1, datetime.date(2025, 8, 22))
    tarea2 = Tarea("Investigar las CNN´s ", 0)
    
    gestor.anadir_tarea(tarea1)
    gestor.anadir_tarea(tarea2)

    gestor.mostrar_tareas()

    print("\nCompletando la primera tarea...")
    gestor.completar_tarea(0)

    gestor.mostrar_tareas()

    print("\nEliminando la segunda tarea...")
    gestor.eliminar_tarea(1)

    gestor.mostrar_tareas()"""
