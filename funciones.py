x=int(input("indique el primer numero: "))
y=int(input("indique el segundo numero: "))
z=int(input("indique el tercer numero: "))

def max(a,b):
    """ Esta funcion calcula el maximo entre dos numros """
    if a>b:
        maximo=a
    else:
        maximo=b
    return maximo
print("el máximo entre ",x,",",y,"y",z,"es" ,max(max(x,y),z))