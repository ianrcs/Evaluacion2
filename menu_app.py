# Función para agregar una compra a la lista
def agregar_compra(compras):
    compra = int(input("Ingrese el monto de la compra: "))
    compras.append(compra)
    print("Compra agregada correctamente.")

# Función para mostrar las compras
def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        for i, compra in enumerate(compras, 1):
            print(f"Compra {i}: ${compra:.2f}")

# Función para mostrar el total gastado
def mostrar_total(compras):
    total = sum(compras)
    print(f"Total gastado: ${total:.2f}")

# Función principal del programa
def main():
    compras = []
    total_gastado = 0

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_compra(compras)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(compras)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
