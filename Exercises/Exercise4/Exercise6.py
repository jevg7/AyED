class Factura:
    def __init__(self):
        self.__productos = []  # Lista privada para almacenar productos

    def agregar_producto(self, nombre, cantidad, precio, descuento=0):
        """Agrega un producto a la factura."""
        if cantidad <= 0 or precio <= 0 or descuento < 0:
            print("Error: Los valores de cantidad, precio y descuento deben ser positivos.")
            return
        
        producto = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio,
            "descuento": descuento
        }
        self.__productos.append(producto)
        print(f"Producto {nombre} agregado correctamente.")

    def calcular_total(self):
        """Calcula el total de la factura."""
        total = 0
        for producto in self.__productos:
            subtotal = producto["cantidad"] * producto["precio"]
            descuento = subtotal * (producto["descuento"] / 100)
            total += (subtotal - descuento)
        return total

    def generar_reporte(self):
        """Genera un reporte detallado de la factura."""
        print("\n--- Factura Detallada ---")
        for producto in self.__productos:
            print(f"Producto: {producto['nombre']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Precio unitario: ${producto['precio']:.2f}")
            print(f"Descuento: {producto['descuento']}%")
            subtotal = producto["cantidad"] * producto["precio"]
            descuento = subtotal * (producto["descuento"] / 100)
            print(f"Subtotal: ${subtotal:.2f} - Descuento: ${descuento:.2f}")
            print("----------------------")
        print(f"Total a pagar: ${self.calcular_total():.2f}")

# Función para ingresar datos desde el usuario
def main():
    factura = Factura()
    
    while True:
        print("\n--- Agregar producto ---")
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio unitario: "))
        descuento = float(input("Descuento (%): "))
        
        factura.agregar_producto(nombre, cantidad, precio, descuento)
        
        otro = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
        if otro != 's':
            break
    
    factura.generar_reporte()

# Ejecutar el programa
if __name__ == "__main__":
    main()
