def hanoi(n):
    if n==1:
        return 2**n-1
    else:
        x=2**(n-1)
        return x+hanoi(n-1)
def main():
    x=int(input())
    print(hanoi(x))
main()
