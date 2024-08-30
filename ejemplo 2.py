continuar = True

while continuar:
    valor = float(input("Ingrese el valor en pesos colombianos: ")) #(1. Tiene que recibir un valor en pesos colombianos)
    
    if valor < 100: #(1.1 Si el valor es menor a 100, ya que es un valor no válido en el peso colombiano muestre un mensaje que pida un valor mayor a 100)
        print("Valor no válido. Ingresa un valor mayor a 100.")
        continue  

    if valor > 85000: #(2. Si el valor es superior a 85.000 le vamos a restar el 2.37% como promoción)
        descuento = valor * 0.0237
        valor -= descuento
    else:
        descuento = 0
    
    if valor > 92000: #(3. Sólo se sumará el iva si el valor supera los 92.000)
        iva = valor * 0.19
    else:
        iva = 0
    
    total = valor + iva
    
    print("Detalles de la operación:")
    print("Valor base: ",valor + descuento) #(4. Indique valor base)
    if iva > 0:
        print("Valor del IVA: ",iva) #(4.1 Indique el valor del iva - Solo si aplica)
    if descuento > 0:
        print("Valor del descuento por promoción:",descuento) #(4.2 Indique el valor del descuento por promocion - Solo si aplica)
    print("Total a pagar:",total) #(4.3 Indique el total)
    
    continuar = False
