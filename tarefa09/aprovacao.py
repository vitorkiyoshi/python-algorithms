def contarPresenca():
    presenca=[]
    while True:
        try:
            entrada=input()
            presenca.append(entrada)
        except:
            break
    return presenca 
def calcularfrequencia(presencas):  
    frequencia=0
    for i in range(len(presencas)):
        if(presencas[i]=="presente"): 
            frequencia+=1
    frequencia/=len(presencas)
    return frequencia
def separarNotas(tarefas):
    tarefa=[]
    for i in range(1,len(tarefas),2):
        tarefa.append(tarefas[i])
    return tarefa 
def verifAprovacao(freq,tarefas):
    for i in range(len(tarefas)):
        if(tarefas[i]=="D"):
            return True
    if freq<0.75: 
        return True
    return False
def main():
    tarefa=separarNotas(input().split()) 
    presenca=contarPresenca() 
    if verifAprovacao(calcularfrequencia(presenca),tarefa):
        print("Reprovadx")
    else:
        print("Aprovadx")
main()
