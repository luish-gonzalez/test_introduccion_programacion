def menu():
    while True:
        print("==== SISTEMA DE CAJERO AUTOMATICA ====")
        print("1. Consultar saldo.")
        print("2. Depositar dinero.")
        print("3. Retirar dinero.")
        print("0. Salir")

        opcion = int(input("Selecciones una opcion: "))
        if opcion == 1:
            print("opcion 1")
        elif opcion == 2:
            op = depositar()
            print("opcion 2")
        elif opcion == 3:
            print("Opcion 3")
        elif opcion == 0:
            print("Ha seleccionado salir")
            break
        else:
            print("Opcion invalida")

def consultarSaldo():
    saldo = 1000
    while True:
        saldo = saldo + depositar() - retirar()

def saldoGlobal():
    saldo = 1000 + depositar() - retirar()
    return saldo

def depositar():
    depo = float(input("Ingrese el valor a depositar:"))
    saldo = 0
    while depo <= 0:
        print("Valor invalido de deposito")
        break
    else:
        saldo = saldo + depo
        print(saldo)

depositar()

deposito = float(input("Ingrese el valor de deposito: "))
saldoInicial = 1000
if deposito >= 0:
    saldoTotal = saldoInicial + deposito
else:
    print("Valor invalido de deposito")
print(saldoTotal)





                                
                  
