def contadorPresenca():#conta presença
    presenca=[]
    while True:
        try:
            entrada=input()
            presenca.append(entrada)
        except:
            break
    return presenca #retorna vetor com as presenças
def frequencia(presencas):  #calcula frequencia
    frequencia=0
    for i in range(len(presencas)):
        if(presencas[i]=="presente"): 
            frequencia+=1
    frequencia/=len(presencas)
    return frequencia
def notas(tarefas):#separa as notas
    tarefa=[]
    for i in range(1,len(tarefas),2):
        tarefa.append(tarefas[i])
    return tarefa #retorna vetor com as notas das tarefas
def verifAprovacao(freq,tarefas):#verifica se o aluno foi aprovado ou não
    reprovado=False
    for i in range(len(tarefas)):
        if(tarefas[i]=="D"):
            reprovado=True
            break 
    if freq<0.75: #verifica se a frequencia atinge o mínimo
        reprovado=True
    if(reprovado):
        return "Reprovadx"
    else:
        return "Aprovadx"
def main():
    tarefa=notas(input().split()) #entrada tarefas
    presenca=contadorPresenca() #entrada das presencas
    print(verifAprovacao(frequencia(presenca),tarefa)) #faz a saída    
main()
