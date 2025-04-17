hamb = 0
papas = 0
bebida = 0
queso = 0 

# Definición de precios
precio_hamburguesa = 8100.0
precio_coca = 3200.0
precio_papas = 3500.0
precio_queso = 150.0

pedido_cancelado = False

def mostrar_menu():
    pedido.append(1)
    pedido.append(0)
    pedido.append(0)
    pedido.append(0) 
    

#opcion = -1  # Inicializamos con un valor que no sea 0
pedido = []  # Lista para almacenar los pedidos
#while opcion != 0:
mostrar_menu()
    #opcion = int(input("Elige una opción: "))
    #pedido.append(opcion) 

promo_galicia = input("Tienes promo galicia? Si / No: \n")
if promo_galicia.lower() == "si":
    promo_galicia = 1
    promo_otra = 0
else:
    promo_otra = input("Tienes otra promo? Si / No: \n")
    if promo_otra.lower() == "si":
        promo_otra = 1
        promo_galicia = 0
    else:
        promo_otra = 0
        promo_galicia = 0

total =0.0

#quiero recorrer el pedido y sumar los precios de cada item, pero viene en formato de lista con 1 o 0 cada una de las 4 opciones
#este es el formato 1000 que es hamburguesa, 0 bebida, 0 papas, 0 queso

for item in pedido:
    if item == 1:
        hamb = 1
        total +=precio_hamburguesa
    elif item == 2:
        bebida= 1
        total +=precio_coca
    elif item == 3:
        papas= 1
        total +=precio_papas
    elif item == 4:
        queso  = 1
        total +=precio_queso



#for item in pedido:
#    if item == 1:
#        hamb = 1
#        total +=precio_hamburguesa
#    elif item == 2:
#        bebida= 1
#        total +=precio_coca
#    elif item == 3:
#        papas= 1
#        total +=precio_papas
#    elif item == 4:
#        queso  = 1
#        total +=precio_queso

pago_permitido = False
promo_valida = promo_galicia ^ promo_otra


while pago_permitido == False:
    if (queso == 1 and hamb == 0):
        print("Tienes que agregar una hamburguesa para agregar el adicional de queso")
        agregado_ham = input("Deseas agregar una hamburguesa? Si / No: \n")
        if agregado_ham.lower() == "si":
            hamb = 1
        else:
            queso = 0
            print("Se ha eliminado el adicional de queso, se cancelara el pedido")
            pedido.remove(4)
            total -= precio_queso
            pago_permitido = True
            pedido_cancelado = True
    elif (queso == 1 and hamb == 1) or (hamb == 1 or bebida == 1 or papas == 1):
        pago_permitido = True

if pago_permitido:
    if not  pedido_cancelado :
        if promo_valida == False:
             print("Total: ", total)
        else:
            if promo_galicia == 1:
                total = total - (total * 0.1)
                print("Se ha descontado 10% por promo galicia")
                print("Total: ", total)

            else:
                total = total - (total * 0.05)
                print("Se ha descontado 5%")
                print("Total: ", total)

print("Gracias por elegirnos!, te esperamos pronto")

#print("\nTabla de verdad:")
#print("Hamburguesa  | Coca-Cola | Papas Fritas | Queso | Total")
#for i in range(16):
#    binario = f"{i:04b}"    
#    print(f"     {binario[0]}       |     {binario[1]}     |      {binario[2]}       |   {binario[3]}")



 