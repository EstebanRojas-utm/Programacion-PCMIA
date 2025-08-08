party = []
i=0
y=0
while(y!=1) :
    x = input("Ingresa algo requerido para la fiesta de bienvenida: ")
    party.append(x)

    y = int(input("Ingresa 1 si ya no vas agregar mas cosas, presiona cualquier tecla para continuar: "))
  
print("\nLa lista de cosas para la party es: \n", party)
