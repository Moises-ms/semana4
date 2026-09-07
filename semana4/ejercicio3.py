# Solicitud de datos al usuario
product_name = input("Nombre del producto: ")
product_price = float(input("Precio unitario: C$ "))
product_quantity = int(input("Cantidad: "))

def calculate_subtotal(price, quantity):
    subtotal_val = price * quantity
    return subtotal_val

def calculate_discount(subtotal):
    if subtotal >= 3000:
        discount_val = subtotal * 0.08
    else:
        discount_val = 0.0
    return discount_val

def calculate_vat(amount):
    vat_val = amount * 0.15
    return vat_val

def display_summary(product, subtotal, discount, vat, total):
    print("\n--- RESUMEN DE COMPRA ---")
    print("Producto:", product)
    print("Subtotal: C$", round(subtotal, 2))
    print("Descuento (8%): C$", round(discount, 2))
    print("IVA (15%): C$", round(vat, 2))
    print("Total a pagar: C$", round(total, 2))