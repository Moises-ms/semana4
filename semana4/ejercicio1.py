def calcular_pago(horas, tarifa):
    pago = horas * tarifa
    return pago


# Guardamos el resultado devuelto en una variable del ámbito global
total_pago = calcular_pago(40, 120)
print("Pago fuera de la función: C$", total_pago)

ventas_registradas = 0

def registrar_venta():
    global ventas_registradas
    ventas_registradas += 1
    print("Venta registrada")


registrar_venta()
registrar_venta()

print("Total de ventas:", ventas_registradas)

def procesar_venta(subtotal):
    def calcular_iva():
        return subtotal * 0.15

    iva = calcular_iva()
    return subtotal + iva


total = procesar_venta(2000)
print("Total: C$", total)

# calcular_iva() no está disponible fuera de procesar_venta.
