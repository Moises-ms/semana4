# Solicitud de datos al usuario
product_name = input("Nombre del producto: ")
product_price = float(input("Precio unitario: C$ "))
product_quantity = int(input("Cantidad: "))

def calculate_subtotal(price, quantity):
    subtotal_val = price * quantity
    return subtotal_val

