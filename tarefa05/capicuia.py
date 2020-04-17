numero= int(input());
numeroString=str(numero);
if len(numeroString)<=4:
    if len(numeroString)==1:
        print("sim")
    elif len(numeroString)==2:
        if numeroString[0]==numeroString[1]:
            print("sim")
        else:
            print("não")
    elif len(numeroString)==3:
        if numeroString[0]==numeroString[2]:
            print("sim")
        else:
            print("não")
    elif len(numeroString)==4:
        if numeroString[0]==numeroString[3] and numeroString[1]==numeroString[2]:
            print("sim")
        else:
            print("não")
