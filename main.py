from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches


print("\t\t\t\t\tBienvenido a LifeStore System\v")
print("\t\t\t\t\tSoftware de analisis de datos\v\v")
print("Si es la primera vez que inicia el programa:\n Su usuario es 'Emtech' y su contraseña es '123' \n")

print("Para continuar inicie sesión")

administradores = [["Emtech","123"],["Oscar","123"]]

usr_inpt = input("Ingresa tu usuario: ")
pss_inpt = input("Ingresa tu contraseña: ")



for usuario in administradores:
  if usuario[0] == usr_inpt and usuario[1] == pss_inpt:
    print("Sesión Iniciada.\n")
    es_admin = 1
    break
  else:
    es_admin = 0  
    continue
  

  

if es_admin == 1:
  print("Bienvenido Administrador: "+ usr_inpt)
  print("\n A continuacion se muestra un menú con la opciones disponibles: \n")
  print("1. Listado de los 50 Productos con mayores ventas.\n2. Listado de los 100 productos con mayores búsquedas. \n3. Listado de los 50 productos con menores ventas.\n4. Listado de los productos que no tivieron ventas.\n5. Listado de los 100 productos con menores búsquedas. ")
  print("\n6. Lista de 20 productos con las mejores reseñas\n7. Lista de 20 productos con las peores reseñas ")
  print("8. Total de ingresos anual.\n   Ventas promedio mensual. \n   Ventas Mensuales \n   Meses con mas ventas en el año")
 

  
  #INICIO DEL CODIGO PARA PODER LEER INDICES Y PRODUCTOS
  contador = 0
  total_ventas = []
  total_compras = []
  for producto in lifestore_products:
    for venta in lifestore_sales:
      if producto[0] == venta[1]:
        contador+=1
    
    formato_ideal = [producto[0], producto[1], contador]
    formato_compras = [contador, producto[0], producto[1]]

    total_ventas.append(formato_ideal)
    total_compras.append(formato_compras)

    contador = 0

  count = 0
  total_busquedas = []
  for product in lifestore_products:
    for busqueda in lifestore_searches:
      if product[0] == busqueda[1]:
        count += 1

    formato_busquedas = [count, product[0], product[1]]
    total_busquedas.append(formato_busquedas)
    count = 0

  #LISTA PARA CONOCER LAS RESEÑAS
  cuenta = 0
  suma = 0
  total_score = []




  for produc in lifestore_products:
    for busque in lifestore_sales:
      if produc[0] == busque[1]:
        cuenta += 1
        suma += busque[2]
        scoreprom = suma / cuenta

    formato_score = [cuenta, produc[0], scoreprom, produc[1]]

    total_score.append(formato_score)
    cuenta = 0
    suma = 0



  #TOTAL DE VENTAS $$$$


  con = 0
  total_com = []
  for produ in lifestore_products:
    for vent in lifestore_sales:
      if produ[0] == vent[1]:
        con += 1

    format_compra = [con, produ[0],produ[2]]
    total_com.append(format_compra)
    con = 0

      





  

  #INICIO DE LOS IF PARA PODER CUMPLIR CON TODOS LOS PARAMETROS SOLICITADOS#

  acción = input("\nSeleccione la letra o numero de la accion a realizar: ")
  if acción == "1":
    

    total_compras.sort(reverse=True)

    masvendidos = []
    i = 0
    x = 0
    while i<50:
      masvendidos.append(total_compras[x])
      x+=1
      i+=1

    n=1
    print("LOS 50 PRODUCTOS MAS VENDIDOS SON:\n ")
    for vistas_ventas in masvendidos:
      print(n,".",vistas_ventas[2], "\nCON UN TOTAL DE: ", vistas_ventas[0]," VENTAS.", "\n SU IDE ES: ", vistas_ventas[1], ".")
      n+=1

  if acción == "2":
    total_busquedas.sort(reverse = True)
    masbuscados = []
    i = 1
    x = 0
    mas = len(total_busquedas)
    if mas <100:
      while i <= mas:
        masbuscados.append(total_busquedas[x])
        x+=1
        i+=1

    if mas > 100:
      while i<100:
        masbuscados.append(total_busquedas[x])
        x+=1
        i+=1
    print("LOS 100 PRODUCTOS MAS BUSCADOS SON:\n ")
    n = 1
    for more_search in masbuscados:
      print(n,". PRODUCTO: ",more_search[2], "\nCON UN TOTAL DE: ", more_search[0], " BUSQUEDAS.", "\nSU ID ES: ", more_search[1],".\n")
      n += 1



  if acción == "3":
    print("Ver los 50 productos menos vendidos que tuvieron minimo 1 venta.")
    respuesta = input("¿Deseas continuar?: [A] = Si  :")
    if respuesta == "A":
      menosventas = []
      total_compras.sort()
      for uno in total_compras:
        while uno[0] != 0:
          menosventas.append(uno)
          break
      n = 1
      print("LOS 50 PRODUCTOS MENOS VENDIDOS SON:\n ")
      for less_sales in menosventas:
        print(n,". PRODUCTO: ",less_sales[2], "\nCON UN TOTAL DE: ", less_sales[0], " VENTAS.", "\nSU ID ES: ", less_sales[1],".\n")
        n +=1

    

  if acción == "4":
    Noventas = []
    print("\nLOS SIGUIENTES PRODUCTOS NO TUVIERON VENTAS: ")
    for nosales in total_ventas:
      if nosales[2] == 0:
        
        print("EL ARTICULO: \n", nosales[1],"\nCUENTA CON:", nosales[2],"VENTAS Y SU ID ES: ", nosales[0],"\n")
        formato_noventas = [nosales[0], nosales[1], nosales[2]]
        Noventas.append(formato_noventas)

  if acción == "5":
    total_busquedas.sort()
    menosbuscados = []
    i = 1
    x = 0
    menos = len(total_busquedas)
    
    if menos < 100:
      while i <= menos:
        menosbuscados.append(total_busquedas[x])
        x+=1
        i+=1

    if menos > 100:
      while i<100:
        menosbuscados.append(total_busquedas[x])
        x+=1
        i+=1
    print("LOS 100 PRODUCTOS MENOS BUSCADOS SON:\n ")
    n = 1
    for less_search in menosbuscados:
      print(n,". PRODUCTO: ",less_search[2], "\nCON UN TOTAL DE: ", less_search[0], " BUSQUEDAS.", "\nSU ID ES: ", less_search[1],".\n") 
      n += 1

  if acción == "6":
    total_score.sort()

    real_score = []
    for puntos in total_score:
      if puntos[0] != 0:

        formato_real_score = [puntos[2], puntos[1], puntos[0], puntos[3]]
        real_score.append(formato_real_score)
    real_score.sort(reverse = True)
    print("LOS 20 PRODUCTOS CON MEJOR SCORE SON: \n")
    b = 0
    n = 1
    for puntaje in real_score:   
      if b<20:
        print(n, ". ", "PRODUCTO: ", puntaje[3], "\nCON UN SCORE DE: " ,puntaje[0], "PUNTOS DE 5 POSIBLES. \n","SU ID ES: ",puntaje[1],"\n")
        n+=1
        b+=1

  if acción == "7":
    total_score.sort()
    real_score = []
    for puntos in total_score:
      if puntos[0] != 0:
        formato_real_score = [puntos[2], puntos[1], puntos[0], puntos[3]]
        real_score.append(formato_real_score)
    real_score.sort()
    print("LOS 20 PRODUCTOS CON EL PEOR SCORE SON: \n")
    b = 0
    n = 1
    for puntaje in real_score:
      if b<20:
        print(n, ". ", "PRODUCTO: ", puntaje[3], "\nCON UN SCORE DE: " ,puntaje[0], "PUNTOS DE 5 POSIBLES. \n","SU ID ES: ",puntaje[1],"\n")
        n+=1
        b+=1

  if acción == "8":
   
    
    monto_total = 0
    for bigtotal in total_com:
      ingresos = bigtotal[0] * bigtotal[2]
      monto_total = monto_total + ingresos

    precio = []
    mes = []
  
    for i in range(0,len(lifestore_products)):
      precio.append(lifestore_products[i][2])
    for i in range(0,len(lifestore_sales)):
      venta2 = lifestore_sales[i][1]-1
      fechav = lifestore_sales[i][3].split("/")[1]
      if len(mes) == 0:
        mes.append([precio[venta2], fechav])
      else:
        bandera = False
        for m in mes:
          if m[1] == fechav:
            m[0] += precio[venta2]
            bandera = True 
        if bandera == False:
          mes.append([precio[venta2], fechav])
    aux=[0,0]
    for i in range (0,len(mes)):
      for j in range (0,len(mes)):
        if(mes[i][1] < mes[j][1]):
          aux[0] = mes[i]
          mes[i] = mes[j]
          mes[j] = aux[0]

    total = 0
    for i in range (0,len(mes)):
      auxi = mes[i][0]
      total = total + auxi
    promedio = total/12

    


    


    print("El total de ventas anual fue de: $", monto_total, "\n")
    print("El promedio de ventas mensuales es de: $", promedio,"\n" )
    for meses in mes:
      print("En el mes", meses[1], "Se obtivieron: $", meses[0])
    
    mes.sort(reverse = True)
    i = 0

    print("\nLos 3 meses con mas ventas en el año fueron: ")
    for mees in mes:
      if i<3:
        print("El mes: ", mees[1], "con: $", mees[0])
        i+=1
      
    


    
else:
  print("Datos no encontrados:")
  print("Su usuario y/o contraseña son incorrectos")


