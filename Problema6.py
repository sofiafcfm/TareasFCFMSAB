peso = float(input("Ingresa tu peso en kilogramos (kg): "))
altura = float(input("Ingresa tu altura en metros (m): "))
imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:.2f}")
if imc < 18.5:
    print("Clasificación: Bajo peso")
elif 18.5 <= imc < 24.9:
    print("Clasificación: Peso normal")
elif 25 <= imc < 29.9:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")
