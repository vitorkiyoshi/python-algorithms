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
        with open(self.arquivo,"r+") as arquivo:
            arquivo.readlines() #colocando ponteiro para o final
            arquivo.write(str(self.id) + ",")
            arquivo.write(self.nome + ",")
            arquivo.write(self.descricao + ",")
            arquivo.write(self.data + ",")
            arquivo.write(self.hora + "\n")
            print("Foi adicionado evento " + str(self.id) + ".")
        pass
    def alterar(self):
        with open(self.arquivo, 'r') as arquivo:
            eventos = arquivo.readlines()
        for i in eventos:
            if str(self.id) in i.split(","):
                index_evento = eventos.index(i)
        with open(self.arquivo, 'w+') as arquivo:
            for linha in eventos:
                if eventos.index(linha) == index_evento:
                    arquivo.write(str(self.id) + ",")
                    arquivo.write(self.nome + ",")
                    arquivo.write(self.descricao + ",")
                    arquivo.write(self.data + ",")
                    arquivo.write(self.hora + "\n")
                    print("Evento "+str(self.id)+" alterado")
                else:
                    arquivo.write(linha)
def inicializar(nome_arquivo):
    with open(nome_arquivo , "w+"):
        print("Uma agenda vazia "+nome_arquivo+" foi criada!")    #inicializa/cria o arquivo csv
    pass

def achar_id_valido(nome_arquivo):
    i=1
    with open(nome_arquivo,"r+") as arquivo:
        try:
            ultimo_id= arquivo.readlines()[-1]
            i = int(ultimo_id.split(",")[0]) + 1
            return i
        except:
            return i

def remover_evento(nome_arquivo, id):
    with open(nome_arquivo,"r") as entrada:
        with open(nome_arquivo+"2","w") as saida:
            for linha in entrada:
                if linha.split(",")[0] != str(id):
                    saida.write(linha)
    os.remove(nome_arquivo)
    os.rename(nome_arquivo+"2",nome_arquivo)
    print("Evento "+str(id)+" removido")
    pass
def identificar_evento(nome_arquivo,id):
    with open(nome_arquivo, "r+") as arquivo:
        while True:
            pesquisa = arquivo.readline().strip().split(",")
            if pesquisa[0] == str(id):
                evento = Evento(id, pesquisa[1], pesquisa[2], pesquisa[3], pesquisa[4], nome_arquivo)
                return evento
def listar_eventos(data, nome_arquivo):
    achou=False
    with open(nome_arquivo,"r+") as arquivo:
        matriz = []
        matriz_data = []
        for linha in arquivo:
            matriz.append(linha.split(","))
        for i in range(len(matriz)):
            if data in matriz[i]:
                achou=True
                matriz_data.append(matriz[i])
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

