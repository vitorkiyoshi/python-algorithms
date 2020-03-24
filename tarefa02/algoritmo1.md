*Algoritmo Para Adição de Datas*
Instruções Elementares:
->Guardar - guardar uma variável, seja ela simples ou vetor.
->Escrever - Retornar algo do programa.
->Separar(caractere)-separa um texto em pedaços por meio de um caractere de separação.
->Comandos matemáticos básicos:
	+=soma
	-=subtração
	*=multiplicação
	/=divisão
->Comando de desvio condicional.

Algoritmo:
Guardar entrada1;
Guardar entrada2;
Separar entrada1(/);
Separar entrada2(/);
saidaDia= entrada1.dia+ entrada2.dia;
saidaMes=0;
saidaAno=0;
SE saidaDia>30
	saidaMes=saidaMes+1
	saidaDia=saidaDia-30;
	Prossiga;
SENÃO 
	Prossiga;
saidaMes=saidaMes+ entrada1.mes+ entrada2.mes;
SE saidaMes>12
	saidaAno=saidaAno+1
	saidaMes=saidaMes-12;
	Prossiga;
SENÃO 
	Prossiga;
saidaAno= saidaAno+ entrada1.ano+ entrada2.ano;
Escrever(saidaDia+"/"+saidaMes+"/"+saidaAno);