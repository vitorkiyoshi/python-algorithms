## Algoritmo Número de Divisores

**Instruções Elementares:**

> Guardar: guarda Entrada.

> Escrever: retorna uma saída.

> Separar(caractere de separação): Torna a variável um vetor, separado por um caractere de separação.

Ex:

	Entrada: "2 3 4"
	variavelX = Guardar(Entrada);
	variavelX.Separar(" ");  #tornando variavelX em vetor separado por um espaço#
	Escrever(variavelX[0]);
	Saída: "2";

> Estrutura vetorial.tamanho: retorna o tamanho do vetor, ou seja, quantos valores existem dentro do vetor.

Ex:

	Entrada: "2 3 4"
	variavelX = Guardar(Entrada);
	variavelX.Separar(" ");  #tornando variavelX em vetor separado por um espaço#
	Escrever(variavelX.tamanho);
	Saída: "3"; #quantos valores existem no vetor#

> iteração condicional.

> desvio condicional.

> iteração limitada.

> operações básicas


**Algoritmo**

	numeros= Guardar;
	numeros.separar(" "); #tornando a variavel numeros um vetor#
	numeroVetor=0;
	qtdeDivisores[];
	divisor=1; 
	repita numeros.tamanho vezes:
		qtdeDivisores[numeroVetor]=0
		enquanto numeros[numeroVetor]>=divisor #iteração condicional do numero do vetor ser diferente do divisor#
			se numeros[numeroVetor]%divisor=0 #desvio convicional de caso o resto da divisão entre numeroVetor e divisor seja 0#
				qtdeDivisores[numeroVetor]=qtdeDivisores[numeroVetor]+1;
				divisor=divisor+1;
			senao
				divisor=divisor+1;
		numeroVetor=numeroVetor+1;
		divisor=1;
	numeroVetor=0;
	saida=0;
	repita qtdeDivisores.tamanho vezes:
		se qtdeDivisores[saida]<qtdeDivisores[numeroVetor] #condição de caso o numero analisado seja maior que o numero esperado para a saída#
			saida=numeroVetor;
			numeroVetor=numeroVetor+1;
		senao
			numeroVetor=numeroVetor+1;
	Escrever(numeros[saida]);