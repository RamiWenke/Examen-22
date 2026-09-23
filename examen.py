# Examen práctico - Sistema de pedidos del kiosco
# Nombre y apellido:ramiro puglisi wenk
# Curso:2o 2
#
# IMPORTANTE:
# Resolver el programa siguiendo las etapas indicadas en el README.md.
# Realizar los commits y push cuando se indique.



# =========================
# ETAPA 1 - INICIO
# =========================

# Crear las variables necesarias.
# Crear las listas de productos y precios.
# Pedir los datos del cliente.


# =========================
# ETAPA 2 - COMPRAS
# =========================

# Mostrar el menú y procesar la opción seleccionada.
# Utilizar las listas para obtener producto y precio.


# =========================
# ETAPA 3 - CICLO PRINCIPAL
# =========================

# Modificar el programa para que continúe funcionando
# hasta que el usuario decida finalizar la compra.


# =========================
# ETAPA 4 - PEDIDO Y RESUMEN
# =========================

# Mostrar el estado actual del pedido.
# Recorrer las listas con un for para mostrar productos y precios.

resp = "hola profe"
dinerogastado = 0
canttotalprodcomp = 0
cantaguascomp = 0
cantalfcomp = 0
canttostcomp = 0
productos = [ "agua", "alfajor", "tostado"]
precio = [ "700", "900", "2200"]
opcion1= 0



nombre = input("¿cual es su nombre?")
platadisp = int(input("¿cuanto dinero tiene para gastar?"))
print("===== KIOSCO ESCOLAR =====")
print(f"hola {nombre}.")
print(f"saldo disponible: ${platadisp}")

while opcion1 != 5 :
 print("1.agua, 2.alfajor, 3.tostado, 4. Consultar pedido, 5. Finalizar compra")

 opcion1 = int(input("¿que opcion desea comprar?"))
 while opcion1 != 1 and opcion1 != 2 and opcion1 != 3 and opcion1 != 4 and opcion1 != 5 :
    print ("opcion no reconocida, debe responer 1, 2 o 3 ")
    opcion1 = int(input("¿que opcion desea comprar?"))
      
     
 if opcion1 == 1 :
    print("producto seleccionado: agua")
    print("precio: $700")
    if platadisp >= 700 :
        print ("compra realizada correctamente")
        platadisp = (platadisp - 700)
        print ("saldo restante:", platadisp) 
        cantaguascomp = cantaguascomp + 1
        dinerogastado = dinerogastado + 700
        canttotalprodcomp = canttotalprodcomp + 1
    else : 
        print ("saldo insuficiente")
     
 elif opcion1 == 2 :
    
    print("producto seleccionado: alfajor")
    print("precio: $900")
    if platadisp >= 900 :
        print ("compra realizada correctamente")
        platadisp = (platadisp - 900)
        print ("saldo restante:", platadisp)
        cantalfcomp = cantalfcomp + 1
        dinerogastado = dinerogastado + 900
        canttotalprodcomp = canttotalprodcomp + 1
    else : 
        print ("saldo insuficiente")
  
 elif opcion1 == 3 :
    
    print("producto seleccionado: tostado")
    print("precio: $2200")
    
    if platadisp >= 2200 :
        print ("compra realizada correctamente")
        platadisp = (platadisp - 2200)
        print ("saldo restante:", platadisp)
        canttostcomp = canttostcomp + 1
        dinerogastado = dinerogastado + 2200
        canttotalprodcomp = canttotalprodcomp + 1
    else : 
        print ("saldo insuficiente")
 
 
 if opcion1 == 4:
    if canttotalprodcomp == 0 :
      print ("el pedido estaba vacio")
    else :
     print("===== PEDIDO ACTUAL =====")
     print(f"hola {nombre}.")
     print(f"productos comprados: {canttotalprodcomp}")
     print(f"dinero gastado: {dinerogastado}")
     print(f"saldo disponible: ${platadisp}")
     print(f"alfajores comprados: {cantalfcomp}")
     print(f"aguas comprados: {cantaguascomp}")
     print(f"tostados comprados: {canttostcomp}")
