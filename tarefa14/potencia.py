def potencia(numero,pot):
    if not pot==0:
        if pot%2==0:
            return potencia(numero,pot/2)*potencia(numero,pot/2)
        else:
            return numero*(potencia(numero,pot-1))
    else:
        return 1
def main():
    numero=input().split()
    n1,n2=int(numero[0]),int(numero[1])
    print(potencia(n1,n2))
main()
