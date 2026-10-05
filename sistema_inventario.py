class Producto:
    def __init__(self, nombre, precio, cantidad):
        # Validamos el nombre
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")

        if nombre.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacío.")

        # Validamos el precio
        if not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser un número.")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        # Validamos la cantidad
        if not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un número entero.")

        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        if not isinstance(nuevo_precio, (int, float)):
            raise TypeError("El nuevo precio debe ser un número.")

        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        self.precio = float(nuevo_precio)

    def actualizar_cantidad(self, nueva_cantidad):
        if not isinstance(nueva_cantidad, int):
            raise TypeError("La nueva cantidad debe ser un número entero.")

        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return (
            f"Producto: {self.nombre} | "
            f"Precio: {self.precio:.2f} € | "
            f"Cantidad: {self.cantidad} | "
            f"Valor total: {self.calcular_valor_total():.2f} €"
        )


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto.")

        self.productos.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto

        return None

    def calcular_valor_inventario(self):
        total = 0

        for producto in self.productos:
            total += producto.calcular_valor_total()

        return total

    def listar_productos(self):
        if len(self.productos) == 0:
            print("\nEl inventario está vacío.")
            return

        print("\n--- PRODUCTOS DEL INVENTARIO ---")

        for producto in self.productos:
            print(producto)


def menu_principal(inventario):
    while True:
        print("\n========== SISTEMA DE INVENTARIO ==========")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            try:
                nombre = input("Nombre del producto: ")

                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad del producto: "))

                producto = Producto(nombre, precio, cantidad)

                inventario.agregar_producto(producto)

                print("\nProducto agregado correctamente.")

            except ValueError as error:
                print(f"\nError: {error}")

            except TypeError as error:
                print(f"\nError: {error}")

        elif opcion == "2":
            try:
                nombre = input("Introduce el nombre del producto a buscar: ")

                producto = inventario.buscar_producto(nombre)

                if producto is None:
                    raise ValueError("Producto no encontrado.")

                print("\nProducto encontrado:")
                print(producto)

            except ValueError as error:
                print(f"\nError: {error}")

        elif opcion == "3":
            inventario.listar_productos()

        elif opcion == "4":
            total = inventario.calcular_valor_inventario()

            print(
                f"\nEl valor total del inventario es: "
                f"{total:.2f} €"
            )

        elif opcion == "5":
            print("\nSaliendo del programa...")
            print("Hasta pronto.")
            break

        else:
            print("\nOpción no válida. Selecciona una opción del 1 al 5.")


if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)