def mdc(n1, n2):
    if n2 == 0:
        return n1
    resto = n1 % n2
    n1,n2=n2,resto
    return mdc(n1,n2)  
        
def main():
    numeros=input().split()
    n1,n2=int(numeros[0]),int(numeros[1])
    divisor=mdc(n1,n2)
    print((n1*n2)//divisor)
main()
    
