class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: ${self.precio:.2f}, Cantidad: {self.cantidad}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            print("El producto ya existe en el inventario.")
        else:
            self.productos[producto.codigo] = producto
            print("Producto agregado exitosamente.")

    def buscar_producto(self, codigo):
        return self.productos.get(codigo, None)

    def actualizar_producto(self, codigo, nuevo_precio=None, nueva_cantidad=None):
        producto = self.buscar_producto(codigo)
        if producto:
            if nuevo_precio is not None:
                producto.actualizar_precio(nuevo_precio)
            if nueva_cantidad is not None:
                producto.actualizar_cantidad(nueva_cantidad)
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

                
if __name__ == "__main__":
    inventario = Inventario()

    p1 = Producto(101, "Laptop", 1200.99, 10)
    p2 = Producto(102, "Mouse", 25.50, 50)

    inventario.agregar_producto(p1)
    inventario.agregar_producto(p2)

    inventario.mostrar_inventario()

    inventario.actualizar_producto(101, nuevo_precio=1100.00)
    inventario.mostrar_inventario()

    inventario.eliminar_producto(102)
    inventario.mostrar_inventario()