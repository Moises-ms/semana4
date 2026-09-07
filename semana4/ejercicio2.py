# --- Ejercicio 1: Modificación de un número (Inmutable) ---
def aumentar_salario(salary):
    salary = salary + 500
    print("Salario dentro de la función:", salary)


original_salary = 2000
aumentar_salario(original_salary)
print("Salario fuera de la función:", original_salary)


# --- Ejercicio 2: Modificación de una lista (Mutable) ---
def agregar_venta(sales_list, new_sale):
    sales_list.append(new_sale)


sales = [100.0, 250.0]
agregar_venta(sales, 400.0)
print("Lista de ventas fuera de la función:", sales)