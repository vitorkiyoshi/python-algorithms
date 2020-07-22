def collatz(n,qtde):
    if n==1:
        return qtde
    if n%2==0:
        return collatz(n/2,qtde+1)
    else:
        return collatz(((n*3)+1)/2,qtde+1)
def main():
    x=int(input())
    print(collatz(x,0))
    
main()
