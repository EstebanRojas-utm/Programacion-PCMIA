
def menu():
    print("\n## Gestor de Tareas Pendientes ##" )
    print("1. Agregar tarea")
    print("2. Insertar tarea")
    print("3. Eliminar por nombre")
    print("4. Eliminar por posicion")
    print("5. Marcar como realizada")
    print("6. Ver tareas")
    print("7. Ordenar tarea")
    print("8. Revertir orden")
    print("9. Salir\n")

def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas.")
    else:
        print("\nLista de tareas:")
        for i, tarea in enumerate(tareas):
            estado = "✔️" if tarea["realizada"] else "❌"
            print(f"{i}. {tarea['nombre']} [ {estado} ]")    

if __name__=='__main__': 
    tareas = []
    opcion = 0
    
    while opcion != 9 :
        menu()
        opcion = int(input("Elige una opcion (1-9): "))

        if opcion == 1:
            nombre = input("Escribe el nombre de la tarea: ")
            tareas.append({"nombre": nombre, "realizada":False})
            print("Tarea agregada.")
        elif opcion == 2:
            nombre = input("Escribe el nombre de la tarea: ")
            try:
                posicion = int(input("Escribe la posición donde insertar: "))
                tareas.insert(posicion, {"nombre": nombre, "realizada": False})
                print("Tarea insertada.")
            except (ValueError, IndexError):
                print("Posición inválida.")

        elif opcion == 3:
            nombre = input("Nombre de la tarea a eliminar: ")
            for tarea in tareas:
                if tarea["nombre"] == nombre:
                    tareas.remove(tarea)
                    print("Tarea eliminada.")
                    break
                else:
                    print("Tarea no encontrada.")
        elif opcion == 4:
            try:
                posicion = int(input("Posición de la tarea a eliminar: "))
                tarea_eliminada = tareas.pop(posicion)
                print(f"Tarea '{tarea_eliminada['nombre']}' eliminada.")
            except (ValueError, IndexError):
                print("Posición inválida.")

        elif opcion == 5:
            try:
                posicion = int(input("Posición de la tarea realizada: "))
                tareas[posicion]["realizada"] = True
                print("Tarea marcada como realizada.")
            except (ValueError, IndexError):
                print("Posición inválida.")

        elif opcion == 6:
            mostrar_tareas(tareas)

        elif opcion == 7:
            tareas.sort(key=lambda x: x["nombre"])
            print("Tareas ordenadas alfabéticamente.")

        elif opcion == 8:
            tareas.reverse()
            print("Orden de tareas invertido.")

        elif opcion == 9:
            print("Saliendo del gestor de tareas. ¡Hasta luego!")

        else:
            print("Opción no válida. Intenta de nuevo.")  

                   


        
        





    
    