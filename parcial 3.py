
numero = input("Ingresa un número: ")#(1. Mostrar un mensaje que pida al usuario un número)
while numero.isdigit() == False: 
    numero = input("Por favor, ingresa un número valido: ") #(1.2 Si se ingresa un valor no esperado pida al usuario que agregue un valor válido)   

numero = int(numero)  
resultado = numero * 2 #(2. Tome el número del usuario y multiplicarlo por 2)

#(2.1 Si el número es múltiplo de 5 Muestre un mensaje que diga "Número redondo". En caso contrario muestre un mensaje que diga "No es múltiplo de 5")
if resultado % 5 == 0:
    print("Número redondo") 
else:
    print("No es múltiplo de 5")

#(3. Ahora tome el resultado de la multiplicación y sumarle 273)
resultado_final = resultado + 273

if resultado_final > 400:
    print("Número grande") # (3.1 Si el número es mayor a 400 muestre un mensaje que diga "Número grande")
else:
    print("Un numero pequeño")#( 3.2 Si es menor a 400 muestre un mensaje que diga "numero pequeño")





