def fibo(n, atual=0, acumulador=None):
    if acumulador is None:
        acumulador = []
    if atual <= 3:
        acumulador.append(atual)
    else:
        acumulador.append(acumulador[atual-1] + acumulador[atual-2] + acumulador[atual-3])
    if atual == n:
        return acumulador[atual]
    else:
        return fibo(n, atual+1, acumulador)    
    
def main():
    n=int(input())
    print(fibo(n))
main()
