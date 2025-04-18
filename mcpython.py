# mcPython.py
#  
import random  # Importamos el módulo random para simular elecciones aleatorias del usuario

# Inicialización de variables (productos y promociones)
hamb = 0            # Hamburguesa
papas = 0           # Papas
bebida = 0          # Bebida
queso = 0           # Queso extra
promo_galicia = 0   # Promoción del banco Galicia
promo_otra = 0      # Otra promoción

# Precios de los productos
precio_hamburguesa = 8100.0
precio_coca = 3200.0
precio_papas = 3500.0
precio_queso = 150.0

# Inicialización del total y controles de estado
total = 0.0
pedido_cancelado = False
pago_permitido = False

# Definición de una función para mostrar el menú
def mostrar_menu():
    global hamb, papas, bebida, queso, promo_galicia, promo_otra


# Mostramos el menú
mostrar_menu()

# Simulación de entrada de datos (elecciones aleatorias del usuario)
hamb = random.randint(0, 1)
papas = random.randint(0, 1)
bebida = random.randint(0, 1)
queso = random.randint(0, 1) 
promo_galicia = random.randint(0, 1)
promo_otra = random.randint(0, 1)

# Mostramos el resumen de lo elegido
print(f"""
    H P B Q PG PO
    {hamb},{papas},{bebida},{queso},{promo_galicia}, {promo_otra}
    """
)

# Calculamos el total sumando los productos seleccionados
if hamb == 1:
    total += precio_hamburguesa
if bebida == 1:
    total += precio_coca
if papas == 1:
    total += precio_papas
if queso == 1:
    total += precio_queso

# Se valida si solo una promoción está activa (XOR bit a bit)
promo_valida = promo_galicia ^ promo_otra

# Validación de reglas antes de permitir pagar
while pago_permitido == False:
    # Si hay queso pero no hay hamburguesa, el usuario debe agregar hamburguesa para continuar
    if (queso == 1 and hamb == 0):
        print("Tienes que agregar una hamburguesa para agregar el adicional de queso")
        agregado_ham = input("¿Deseas agregar una hamburguesa? Si / No: \n")
        
        if agregado_ham.lower() == "si":
            hamb = 1  # Se agrega la hamburguesa
        else:
            queso = 0  # Se elimina el queso
            print("Se ha eliminado el adicional de queso, se cancelará el pedido")
            total -= precio_queso
            pago_permitido = True
            pedido_cancelado = True
    # Si elije hamburguesa y queso o hamburguesa sola o bebida sola o papas sola, se permite pagar
    elif (queso == 1 and hamb == 1) or (hamb == 1 or bebida == 1 or papas == 1):
        pago_permitido = True

# Si el pago está permitido y no se canceló el pedido, se muestra el total
if pago_permitido:
    if not pedido_cancelado:
        #Si no hay promociones válidas devuelve el total
        if promo_valida == False:
            print("Total: ", total)
        else:
            # Sino si elijio una promo aplicamos el descuento 
            if promo_galicia == 1:
                total = total - (total * 0.1)
                print("Se ha descontado 10% por promo Galicia")
                print("Total: ", total)
            else:
                total = total - (total * 0.05)
                print("Se ha descontado 5%")
                print("Total: ", total)

# Mensaje final
print("¡Gracias por elegirnos!, te esperamos pronto")