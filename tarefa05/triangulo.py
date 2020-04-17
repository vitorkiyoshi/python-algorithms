# lê uma string com três partes
a, b, c = input().split()

# converte strings em números
a = float(a)
b = float(b)
c = float(c)
numeroMaior=0
# termine esse programa aqui...
if a+b>c and a+c>b and b+c>a:
    numeroMaior= a;
    if(numeroMaior<b):
        numeroMaior=b;
    if(numeroMaior<c):
        numeroMaior=c;
    if(numeroMaior==a):
        cosseno= -(numeroMaior**2 - (b**2 + c**2))/(2*b*c)
    elif(numeroMaior==b):
        cosseno= -(numeroMaior**2 - (a**2 + c**2))/(2*a*c)
    elif(numeroMaior==c):
        cosseno= -(numeroMaior**2 - (a**2 + b**2))/(2*a*b)
    if(cosseno==0):
        print("retângulo")
    elif(cosseno>0):
        print("acutângulo")
    elif(cosseno<0):
        print("obtusângulo")
else:
    print("não forma triângulo");

