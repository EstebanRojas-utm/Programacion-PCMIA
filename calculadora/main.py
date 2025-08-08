import aritmetica as ari
import multiplicacion_division as md

x1 = int(input("Dame un numero: "))
x2 = int(input("Dame otro numero: "))

print("\nLa suma es: ", ari.fun_suma(x1,x2))
print("\nLa resta es: ", ari.fun_resta(x1,x2))

print("\nLa multiplicacion es: ", md.fun_multi(x1,x2))
print("\nLa division es: ", md.fun_division(x1,x2))