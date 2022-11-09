import Transaccion
import funciones

continuar=True
while(continuar):
    try:
        opc = funciones.menuPrincipal()
        match(opc):
            case 1:
                transferencia = Transaccion.Transferencia()
                cuenta = funciones.ingresoCuenta('19145078912346') #REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                if(transferencia.existeCuenta(cuenta)):
                    try:
                        monto = float(input("Ingrese el monto a depositar: \n"))
                        if (transferencia.montoValido(monto, '19145078912346')):  # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                            transferencia.operacion('19145078912346', cuenta, monto)  # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                            print("¡Transacción completada!\n")
                            fecha, hora = funciones.obtenerTiempo()
                            funciones.mostrarTransferencia(cuenta, monto, fecha, hora)
                            lista = funciones.exportarTransferencia('19145078912346', cuenta, monto, fecha, hora)  # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                            transferencia.mandarDatos(lista)
                            transferencia.cerrarConexion()
                            continue
                        else:
                            continue
                    except ValueError:
                        print("\n ERROR: No puede ingresar variables que no sean números \n")
                else:
                    continue
            case 2:
                retiro = Transaccion.Retiro()
                try:
                    monto = float(input("Ingrese el monto a retirar \n"))
                    if(retiro.montoValido(monto, '19145078912346')): # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                        retiro.operacion('19145078912346',monto) # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                        print("¡Retiro completado!\n")
                        fecha, hora = funciones.obtenerTiempo()
                        saldo = retiro.obtenerSaldo('19145078912346') # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                        funciones.mostrarRetiro(monto, saldo, fecha, hora)
                        lista = funciones.exportarRetiro('19145078912346', monto, fecha, hora) # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                        retiro.mandarDatos(lista)
                        retiro.cerrarConexion()
                        continue
                    else:
                        continue
                except ValueError:
                    print("\n ERROR: No puede ingresar variables que no sean números \n")
                continue
            case 0:
                continuar = False
                continue
            case _:
                print("Ingrese una opción valida... \n")
                continue
    except ValueError:
        print("\n ERROR: No puede ingresar variables que no sean números \n")