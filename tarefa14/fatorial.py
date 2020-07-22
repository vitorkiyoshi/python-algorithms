def fatorial(x):
    if x==0:
        return 1
    if x==1:
        return 1
    n=fatorial(x-1)
    return x*n
def main():
    print(fatorial(int(input())))
main()
