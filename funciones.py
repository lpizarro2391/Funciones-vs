x=(input("indique el primer numero: "))
y=(input("indique el segundo numero: "))
def max(a,b):
    """ Esta funcion calcula el maximo entre dos numros """
    if a>b:
        maximo=a
    else:
        maximo=b
    return maximo
print("el máximo entre ",x,"y",y,"es",max(x,y))   
