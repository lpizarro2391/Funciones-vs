bitcoin=float(input("ingrese la cantidad de bitcoin"))
ethereum=float(input("ingrese la cantidad de ethereum"))
litecoin=float(input("ingrese la cantidad de litecoin"))
totalEUR=0
def ConversionCriptomoneda(bitcoin, ethereum, litecoin):
    ltcEUR=104.50
    btcEUR=6500.81
    ethEUR=493.35
    totalEUR=(bitcoin*btcEUR)+(ethereum*ethEUR)+(litecoin*ltcEUR)
    print("el total de criptomonedas es",totalEUR)
ConversionCriptomoneda(bitcoin,ethereum, litecoin)