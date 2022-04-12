#PROGRAMA PARA CONVERTIR MONEDAS
#VERSION 1.0 - CONVERTIR DE SOLES A DOLARES
#INPUTS - ENTRADAS
montoSoles = input("Ingrese el nomto en soles: ")
#PROCESO
montoDolares = float(montoSoles) / 3.80
montoDolaresFormato = "$ {:,.2f}".format(montoDolares)
#OUTPUTS - SALIDAS
print("El monto en dolares es: " + str(montoDolaresFormato))
print("El monto en dolares es: " + str(round(montoDolares,2)))
