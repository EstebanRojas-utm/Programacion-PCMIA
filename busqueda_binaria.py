objetive = int(input('Introducir un número entero: '))
epsilon = 0.01
lower_limit = 0.0
upper_limit = max(1.0, objetive)
solution = (upper_limit + lower_limit) / 2
contador = 0

while abs(solution**2 - objetive) >= epsilon:
    contador += 1
    if solution**2 < objetive:
        lower_limit = solution
    else:
        upper_limit = solution
    solution = (upper_limit + lower_limit) / 2

print(f'La raíz cuadrada de {objetive} es ~ {solution}')
print(f"Número de evaluaciones: {contador}")
