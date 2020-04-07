## Problema da Adição de Data

Para o problema dado, no qual deve-se haver como entrada duas datas para que posteriormente haja adição, dado o exemplo:

	Entrada:
		11/09/1920
		12/03/2030
Tem-se como seguintes **processos**:

>Adiciona-se as duas datas de acordo com a cronologia(adiciona-se os dias, os meses e os anos respectivamente)

>Caso o dia supere o número 30, adiciona-se 1 no local do mês e subtrai-se 30 do dia.

>Caso o mês supere o número 12, adiciona-se 1 no local do ano e subtrai-se 12 do mês.

Logo, nenhum mês pode superar sua quantidade(que seria 12) e a quantidade de dias não pode ultrapassar o equivalente ao mês,
sendo considerado 30 dias o equivalente a um mês. 

Após o processo de adição, deve-se retornar como saída a data adicionada, segundo o exemplo:

	Saída:
		23/12/3950