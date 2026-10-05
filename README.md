# sistema-inventario-python
Sistema básico de inventario desarrollado en Python utilizando programación orientada a objetos.
# Sistema de inventario en Python

Este proyecto consiste en un sistema básico de inventario desarrollado en Python utilizando programación orientada a objetos.

El programa permite crear productos con su nombre, precio y cantidad, almacenarlos en un inventario y realizar diferentes operaciones con ellos desde un menú por consola.

## Funcionalidades

El programa permite:

- Agregar nuevos productos al inventario.
- Buscar un producto por su nombre.
- Mostrar todos los productos guardados.
- Calcular el valor total del inventario.
- Comprobar que los datos introducidos sean válidos.
- Controlar errores mediante excepciones.

## Estructura del programa

El programa está organizado principalmente en dos clases:

### Producto

Representa cada producto del inventario y almacena su nombre, precio y cantidad.

También contiene métodos para actualizar el precio o la cantidad y para calcular el valor total de un producto.

### Inventario

Se encarga de almacenar y gestionar los productos.

Permite añadir productos, buscarlos por su nombre, mostrar el contenido del inventario y calcular el valor total de todos los productos almacenados.

## Ejecución

Para ejecutar el programa es necesario tener Python instalado.

Desde una terminal situada en la carpeta del proyecto se puede ejecutar con:

```bash
python sistema_inventario.py