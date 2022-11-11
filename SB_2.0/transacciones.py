import transaccion
import funciones
def transacciones(dni):
    continuar=True
    while(continuar):
        try:
            opc = funciones.menuPrincipal()
            match(opc):
                case 1:
                    deposito = transaccion.Deposito()
                    try:
                        monto = float(input("Ingrese el monto a depositar \n"))
                         # REEMPLAZAR
                        deposito.operacion(monto, dni) # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                        print("¡Depósito completado! \n")
                        fecha, hora = funciones.obtenerTiempo()
                        ID = "0" + funciones.generarNumero(9)
                        while (deposito.existeID(ID)):
                            ID = "0" + funciones.generarNumero(9)
                        funciones.mostrarDeposito(ID, monto, fecha, hora)
                        lista = funciones.exportarDeposito(ID, dni,monto, fecha, hora)
                        deposito.mandarDatos(lista)
                        deposito.cerrarConexion()
                        continue
                    
                    except ValueError:
                        print("\n ERROR: No puede ingresar variables que no sean números \n")
                    continue
                case 2:
                    transferencia = transaccion.Transferencia()
                    cuenta = funciones.ingresoCuenta(dni) #REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                    if(transferencia.existeCuenta(cuenta)):
                        try:
                            monto = float(input("Ingrese el monto a depositar: \n"))
                            if (transferencia.montoValido(monto, dni)):  # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                                transferencia.operacion(dni, cuenta, monto)  # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                                print("¡Transacción completada!\n")
                                fecha, hora = funciones.obtenerTiempo()
                                ID = "1" + funciones.generarNumero(9)
                                while(transferencia.existeID(ID)):
                                    ID = "1" + funciones.generarNumero(9)
                                funciones.mostrarTransferencia(cuenta, monto, ID, fecha, hora)
                                lista = funciones.exportarTransferencia(ID, dni, cuenta, monto, fecha, hora)  # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                                transferencia.mandarDatos(lista)
                                transferencia.cerrarConexion()
                                continue
                            else:
                                continue
                        except ValueError:
                            print("\n ERROR: No puede ingresar variables que no sean números \n")
                    else:
                        continue
                case 3:
                    retiro = transaccion.Retiro()
                    try:
                        monto = float(input("Ingrese el monto a retirar \n"))
                        if(retiro.montoValido(monto, dni)): # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                            retiro.operacion(dni,monto) # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                            print("¡Retiro completado!\n")
                            fecha, hora = funciones.obtenerTiempo()
                            ID = "2" + funciones.generarNumero(9)
                            while(retiro.existeID(ID)):
                                ID = "2" + funciones.generarNumero(9)
                            saldo = retiro.obtenerSaldo(dni) # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                            funciones.mostrarRetiro(monto, saldo, ID, fecha, hora)
                            lista = funciones.exportarRetiro(ID,dni, monto, fecha, hora) # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                            retiro.mandarDatos(lista)
                            retiro.cerrarConexion()
                            continue
                        else:
                            continue
                    except ValueError:
                        print("\n ERROR: No puede ingresar variables que no sean números \n")
                    continue
                case 4:
                    pagoServicios = transaccion.pagoServicios(dni) #REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE!!!
                    deudas = pagoServicios.devolverDeudas()
                    funciones.mostrarDeudas(deudas)
                    try:
                        codigoDeuda = funciones.ingresoDeuda()
                        if (not pagoServicios.existeID(codigoDeuda)):
                            print("\n Este codigo no existe...\n \n")
                            continue
                        else:
                            monto = pagoServicios.deudaMonto(codigoDeuda)
                            if(pagoServicios.montoValido(monto,dni)): # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                                pagoServicios.operacion(dni,monto, codigoDeuda) # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                                print("¡Servicio cancelado! \n")
                                fecha, hora = funciones.obtenerTiempo()
                                ID = "3" + funciones.generarNumero(9)
                                while(pagoServicios.existeID(ID)):
                                    ID = "3" + funciones.generarNumero(9)
                                funciones.mostrarServicio(ID, fecha, hora)
                                lista = funciones.exportarServicio(ID, codigoDeuda, dni, monto, fecha, hora) # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                                pagoServicios.mandarDatos(lista)
                                pagoServicios.cerrarConexion()
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
