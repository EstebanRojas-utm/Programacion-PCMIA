"""
#Metodo de aproximacion
objetive = int(input('Introduce un número entero:'))
epsilon = 0.001 #0.0001
step = epsilon**2
solution = 0.0

while abs(solution**2 - objetive) >= epsilon and solution <= objetive:
   print(abs(solution**2 - objetive), objetive)
   solution += step

if abs(solution**2 - objetive) >= epsilon:
   print(f'No se encontro la raíz cuadrada de {objetive}')
else:
   print(f'La raíz cuadrada de {objetive} es ~ {solution}')"""

objetive = int(input('Introducir un número entero:'))
epsilon = 0.00000000001
lower_limit = 0.0
upper_limit = max(1.0, objetive)
step = epsilon**2
solution = (upper_limit + lower_limit) / 2

i=0

while abs(solution**2 - objetive) >= epsilon:
    if solution**2 < objetive:
        lower_limit = solution
    else:
        upper_limit = solution    
    
    solution = (upper_limit + lower_limit) / 2
    i= i+1

print(f'La raíz cuadrada de {objetive} es ~ {solution}')
print("El numero de ocasiones que evalua es: ",i)