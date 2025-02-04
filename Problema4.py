precio = float(input("Ingresa el precio del producto: "))
descuento = float(input("Ingresa el porcentaje de descuento: "))
monto_descuento = precio * (descuento / 100)
precio_final = precio - monto_descuento
print(f"El precio original es: ${precio:.2f}")
print(f"El descuento aplicado es: ${monto_descuento:.2f}")
print(f"El precio final después del descuento es: ${precio_final:.2f}")
