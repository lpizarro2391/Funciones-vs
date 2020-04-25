def esmoneda(cripto):
    criptos = ["BTC","BCC","LTC","ETH","ETC","XRP"]
    if cripto in criptos:
        return True
    else:
        return False
def esnumero(numero):
    return numero.replace('.','',1).isdigit()
i=0
total=0
while (i < 3):
    cripto = input("Ingrese el nombre de la moneda: ")
    if esmoneda(cripto):
        i = i + 1
        cant= " "
        while not esnumero(cant):
            cant = input("Indique la cantidad de "+cripto+":")
        cotiz=""
        while not esnumero(cotiz):
            cotiz = input("Indique la Cotizacion de "+cripto+":")
        total = total + float(cant) * float (cotiz) 
    else:
        print("Moneda Inválida.")
print("El total en USD que tiene el usuario es de ",str(total))
