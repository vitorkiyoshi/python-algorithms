import argparse
import os   #para renomear e excluir arquivo
class Evento:
    def __init__(self, id , nome, descricao, data, hora, arquivo):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.data = data
        self.hora = hora
        self.arquivo = arquivo
    def criar(self):
        matriz=carregar_arquivo(self.arquivo)
        matriz.append([self.id,self.nome,self.descricao,self.data,self.hora])
        salvar_arquivo(matriz,self.arquivo)
        print("Evento com id"+str(self.id)+"criado")
    def alterar(self):
        matriz=carregar_arquivo(self.arquivo)
        for i in range(len(matriz)):
            if matriz[i][0]==str(self.id):
                matriz[i][1]=self.nome
                matriz[i][2]=self.descricao
                matriz[i][3]=self.data
                matriz[i][4]=self.hora
                salvar_arquivo(matriz,self.arquivo)
                print("Evento "+str(self.id)+" alterado")
                
def carregar_arquivo(nome_arquivo):
    matriz_agenda=[]
    with open(nome_arquivo,"r+") as arquivo:
        for linha in arquivo:
            matriz_agenda.append(linha.strip().split(","))
    return matriz_agenda
def salvar_arquivo(matriz,nome_arquivo):
    with open(nome_arquivo,"w+") as arquivo:
        for linha in matriz:
            arquivo.write(str(linha[0]) + ",")
            arquivo.write(linha[1] + ",")
            arquivo.write(linha[2] + ",")
            arquivo.write(linha[3] + ",")
            arquivo.write(linha[4] + "\n")
    pass
    
def remover_evento(nome_arquivo,id):
    matriz=carregar_arquivo(nome_arquivo)
    for i in range(len(matriz)):
        if matriz[i][0]==str(id):
            del matriz[i]
            break
    salvar_arquivo(matriz,nome_arquivo)
    print("removido evento"+str(id))
    pass
    
def inicializar(nome_arquivo):
    with open(nome_arquivo , "w+"):
        print("Uma agenda vazia "+nome_arquivo+" foi criada!")    #inicializa/cria o arquivo csv
    pass

def achar_id_valido(nome_arquivo):
    matriz=carregar_arquivo(nome_arquivo)
    if matriz==[]:
        return 1
    else:
        return len(matriz)+1
    
def identificar_evento(nome_arquivo,id):
    matriz=carregar_arquivo(nome_arquivo)
    for i in range(len(matriz)):
        if matriz[i][0]==str(id):
            evento = Evento(id, matriz[i][1], matriz[i][2], matriz[i][3], matriz[i][4], nome_arquivo)   #retornando objeto evento do arquivo csv
            return evento
def listar_eventos(data, nome_arquivo):
    achou=False
    matriz=carregar_arquivo(nome_arquivo)
    matriz_data = []
    for i in range(len(matriz)):
        if str(data) in matriz[i]:
            matriz_data.append(matriz[i])
            achou=True
    if achou:
        print("Eventos do dia " + data)
        print("-----------------------------------------------")
        for i in range(len(matriz_data)):
            print("Evento "+matriz_data[i][0]+" - "+matriz_data[i][1])
            print("Descrição: "+matriz_data[i][2])
            print("Data: "+matriz_data[i][3])
            print("Hora: "+matriz_data[i][4])
            print("-----------------------------------------------")
            pass
    else:
        print("Não existem eventos para o dia "+data+"!")
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--arquivo", help="nome do arquivo.", type=str)
    parser.add_argument("acao", help="acao no arquivo.", type=str)
    parser.add_argument("--nome", help="nome da tarefa.", type=str)
    parser.add_argument("--descricao", help="descricao da tarefa.", type=str)   #pegando argumentos
    parser.add_argument("--data", help="data da tarefa.", type=str)
    parser.add_argument("--hora", help="hora da tarefa.", type=str)
    parser.add_argument("--evento", help="id.", type=int)
    args = parser.parse_args()
    if args.acao == "inicializar":
        inicializar(args.arquivo)
    if args.acao == "criar":
        evento = Evento(achar_id_valido(args.arquivo), args.nome, args.descricao, args.data, args.hora, args.arquivo)  #criando objeto
        evento.criar()
    if args.acao == "remover":
        remover_evento(args.arquivo, args.evento)
    if args.acao == "alterar":
        evento = identificar_evento(args.arquivo, args.evento)
        if args.nome is not None:
            evento.nome = args.nome
        if args.descricao is not None:
            evento.descricao = args.descricao
        if args.data is not None:
            evento.data = args.data
        if args.hora is not None:
            evento.hora = args.hora
        evento.alterar()
    if args.acao == "listar":
        listar_eventos(args.data, args.arquivo)
main()

