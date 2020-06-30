**Algoritmo agenda.py**
### Formatação
o algoritmo tem como propósito armazenar eventos em um arquivo csv, tal arquivo  contém 5 colunas, sem rodapé e cabeçalho, sendo organizadas respectivamente em: 
 
 `numero do evento(id),nome do evento,descrição,data,hora`

cada coluna é separada por uma vírgula(`,`), enquanto que cada evento é separado por uma quebra de linha(`"\n"`).
### Estrutura de dados
O algoritmo agenda.py possui uma classe Evento, na qual são declarados novos objetos e manipulação destes a partir dos argumentos mandados pelo usuário. Porém fica implícito a inserção do número do evento(id), no qual o programa deve identificar o id a ser colocado no arquivo csv.
Para isso, a classe Evento então tem como atributos:
- id: int, seria o número do evento;
- nome: string
- descricao: string
- data: string
- hora: string
- arquivo: string(nome do arquivo onde está armazenado o evento)

### Utilização

O algoritmo tem como Ação diretriz o argumento dado pelo usuário. Assim, tem-se como instruções:
Os atributos no algoritmo possuem 2 tipos de argumentações:
- Posição(ação): Coloca-se apenas como parâmetro uma das ações programadas.
- Opção: Coloca-se antes do parâmetro o argumento atribuído para a informação.
Nome do arquivo: `-a <nome do arquivo>`
Nome do evento:  `--nome <nome do evento>`
Descrição do evento: `--descricao <descricao do evento>`
Data do evento: `--data <data do evento>`
Hora do Evento: `--hora <hora do evento>`
Número do evento: `--evento <numero do evento>`
 

Assim, o algoritmo pode realizar as seguintes ações:
- inicializar: Sintetiza um arquivo em branco no formato .csv.
Exemplo de Uso: `python3 agenda.py -a agenda.csv inicializar`
Mensagem de retorno: `Uma agenda vazia 'agenda.csv' foi criada!`
- criar: Cria um evento e seu número no arquivo .csv, precisando especificar os atributos necessários para a criação do objeto evento, com exceção do número.
Exemplo de Uso: `python3 agenda.py -a agenda.csv criar --nome "MC102" --descricao "Aula de laboratório" --data "01/06/2020" --hora "14:00"`
Mensagem de Retorno: `Foi adicionado evento 1.`

- alterar: Altera um evento dentro do arquivo .csv, especificando o número do arquivo a ser alterado e os atributos a serem alterados.
Exemplo de Uso: `python3 agenda.py -a agenda.csv alterar --evento 1 --hora "16:00"`
Mensagem de Retorno: `Evento 1 alterado.`
- Remover: Remove um evento do arquivo csv. especificando o número do evento a ser removido.
Exemplo de Uso: `python3 agenda.py -a agenda.csv remover --evento 1 `
Mensagem de Retorno: `Evento 1 removido.`
- Listar: Lista os eventos de tal data no arquivo .csv, especificando a data a ser pesquisada.
Exemplo de Uso: `python3 agenda.py -a agenda.csv listar --data '19/03/2020'`
Mensagem de Retorno: Caso existam eventos, serão listados em ordem crescente do número do evento, do contrário,
`Não existem eventos para o dia <data>.`