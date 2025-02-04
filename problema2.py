num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Determinar cuál es el mayor, menor o si son iguales
if num1 > num2:
    print(f"El número mayor es {num1} y el número menor es {num2}.")
elif num1 < num2:
    print(f"El número mayor es {num2} y el número menor es {num1}.")
else:
    print("Los números son iguales.")
