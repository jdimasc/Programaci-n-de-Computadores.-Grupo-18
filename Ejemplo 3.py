

temperatura = float(input("Ingrese la temperatura: ")) #(1. Pida al usuario un número que será la temperatura)
unidad_inicial = input("Seleccione la unidad inicial (Celsius, Fahrenheit, Kelvin): ").lower() #(2. Le daremos 3 opciones para seleccionar 
#si es Celsius, fahrenheit y Kelvin )
if unidad_inicial not in ['celsius', 'fahrenheit', 'kelvin']:
    print("Unidad inválida. Se tomará Celsius por defecto.") #(2.2 Si pone un valor no esperado, le daremos un valor por defecto que será Celsius)
    unidad_inicial = 'celsius'

unidad_destino = input("Seleccione la unidad de destino (Celsius, Fahrenheit, Kelvin): ").lower()

if unidad_destino not in ['celsius', 'fahrenheit', 'kelvin']:
    print("Unidad no válida. Se tomará Celsius por defecto.")
    unidad_destino = 'celsius'

if unidad_inicial == 'celsius':
    if unidad_destino == 'fahrenheit':
        resultado = temperatura * 9/5 + 32
    elif unidad_destino == 'kelvin':            #(3 convertir a celsius)
        resultado = temperatura + 273.15
    else:
        resultado = temperatura 
elif unidad_inicial == 'fahrenheit':
    if unidad_destino == 'celsius':
        resultado = (temperatura - 32) * 5/9    #(3.1 Convertir fahrenheit)
    elif unidad_destino == 'kelvin':
        resultado = (temperatura - 32) * 5/9 + 273.15
    else:
        resultado = temperatura  
elif unidad_inicial == 'kelvin':
    if unidad_destino == 'celsius':
        resultado = temperatura - 273.15
    elif unidad_destino == 'fahrenheit':        #(3.2 Convertir a Kelvin)
        resultado = (temperatura - 273.15) * 9/5 + 32
    else:
        resultado = temperatura  # Kelvin a Kelvin


print("La temperatura en", unidad_destino.capitalize(), "es:", f"{resultado:.2f}")


