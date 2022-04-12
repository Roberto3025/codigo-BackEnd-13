#PROGRAMA PARA CONVERTIR MONEDAS
#VERSION 1.0 - CONVERTIR DE SOLES A DOLARES
#INPUTS - ENTRADAS
opcion = 0
while(opcion == 0):
    print("=========== OPCIONES ============")
    print("Opcion 1 - Soles a Dolares")
    print("Opcion 2 - Dolares a Soles")
    print("Opcion 3 - Soles a Euros")
    print("Opcion 4 - Euros a Soles")
    print("Opcion 5 - Salir")
    opcion = input("Eliga una opcion: ")
    monto = input("Ingrese el nomto en soles: ")
    #PROCESO
    if(opcion == "1"):
        montoDolares = float(monto) / 3.80
        #OUTPUTS - SALIDAS
        print("El monto en dolares es: $ " + str(round(montoDolares,2)))
        opcion = 0
    elif(opcion == "2"):
        montoSoles = float(monto) * 3.80
        montoDolaresFormato = "S/ {:,.2f}".format(montoSoles)
        #OUTPUTS - SALIDAS
        print("El monto en Soles es: ", montoDolaresFormato)
        opcion = 0
    elif(opcion == "3"):
        montoSolEuro = float(monto) / 4.05
        #OUTPUTS - SALIDAS
        print("El monto en Euros es: E " + str(round(montoSolEuro,2)))
        opcion = 0
    elif(opcion == "4"):
        montoEuroSol = float(monto) * 4.05
        montoEuroFormato = "S/ {:,.2f}".format(montoEuroSol)
        #OUTPUTS - SALIDAS
        print("El monto en Eruros es: ", montoEuroFormato)
        opcion = 0
    elif(opcion == "5"):
        salir = input("Desea salir si/no: ")
        if(salir == "no"):
            opcion = 0
        else:
            print("Exit")
    else:
        print("ALERTA!!!, debe seleccionar una opcion valida")
        opcion = 0

