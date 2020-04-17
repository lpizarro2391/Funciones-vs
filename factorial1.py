n=int(input("indique el numero a calcular el factorial"))
def factorial_rec(n):
   if n == 0:
     return 1
   else:
        return n * factorial_rec(n-1)
print("El factorial de",n,"es",factorial_rec(n))