class Cliente:
    def __init__(self, id_cliente, nombre, contacto):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.contacto = contacto
    
    def obtener_descuento(self, total):
        return 0  # No hay descuento por defecto
    
    def __str__(self):
        return f"Cliente {self.id_cliente}: {self.nombre} ({self.contacto})"

class ClienteVIP(Cliente):
    def obtener_descuento(self, total):
        return total * 0.10  # 10% de descuento para clientes VIP
    
    def __str__(self):
        return f"Cliente VIP {self.id_cliente}: {self.nombre} ({self.contacto})"

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []
        self.total = 0
    
    def agregar_producto(self, producto, precio, cantidad):
        self.productos.append((producto, precio, cantidad))
        self.total += precio * cantidad
    
    def calcular_total_con_descuento(self):
        descuento = self.cliente.obtener_descuento(self.total)
        return self.total - descuento
    
    def mostrar_pedido(self):
        print("\nResumen del Pedido:")
        print(self.cliente)
        print("Productos:")
        for producto, precio, cantidad in self.productos:
            print(f"- {producto} (x{cantidad}) - ${precio:.2f} c/u")
        print(f"Total antes de descuento: ${self.total:.2f}")
        print(f"Total después de descuento: ${self.calcular_total_con_descuento():.2f}")

# Función para ingresar datos y crear pedidos
def main():
    clientes = []
    print("Registro de Cliente")
    id_cliente = input("Ingrese ID del cliente: ")
    nombre = input("Ingrese nombre del cliente: ")
    contacto = input("Ingrese contacto del cliente: ")
    tipo = input("¿Es cliente VIP? (s/n): ")
    
    if tipo.lower() == 's':
        cliente = ClienteVIP(id_cliente, nombre, contacto)
    else:
        cliente = Cliente(id_cliente, nombre, contacto)
    
    clientes.append(cliente)
    pedido = Pedido(cliente)
    
    while True:
        producto = input("Ingrese nombre del producto (o 'fin' para terminar): ")
        if producto.lower() == 'fin':
            break
        precio = float(input("Ingrese precio del producto: "))
        cantidad = int(input("Ingrese cantidad: "))
        pedido.agregar_producto(producto, precio, cantidad)
    
    pedido.mostrar_pedido()

if __name__ == "__main__":
    main()
