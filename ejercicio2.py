"""cube = int(input("Ingresar un entero:"))

for guess in range(cube+1):
    if guess**3 == cube:
        print("La raiz cubica de ", cube, " es ", guess)
"""

"""x = 0.12
for i in range(10):
   x += 0.1
print(x == 1)
print(x, "==", 10 * 0.1)"""

"""
#Conversion decimal a flotante 
num = 10
result = ''

if num == 0:
   result = '0'

while num > 0:
   result = str(num%2) + result
   num = num // 2

print(result)  """

#Representacion binaria del decimal
x = 10.625

p = 0
while ((2**p)*x) % 1 != 0:
    print('Resto = ' + str((2**p)*x - int((2**p)*x)))
    p += 1

num = int(x * (2**p))

resultado = ''
if num == 0:
    resultado = '0'
while num > 0:
    resultado = str(num % 2) + resultado
    num = num // 2

for i in range(p - len(resultado)):
    resultado = '0' + resultado

resultado = resultado[0:-p] + '.' + resultado[-p:]
print("Resto = " + str((2**p)*x - int((2**p)*x)) )
print('\nLa representación binaria del decimal ' + str(x) + ' es ' + str(resultado))























