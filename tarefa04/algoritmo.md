## Algoritmo Baldes de Água
**Instruções Elementares:**
>Despejar (<balde1> em <balde 2>) : despeja a quantidade de liquido num balde1 num balde2.

>iteração condicional: repetição do comando até que a condição seja atingida.

>Verificar(balde): Verifica se o balde está com 1 litro.

>Saida(balde) 

**Algoritmo**
	
	```enquanto balde A não estiver cheio:	//Enchendo balde A de agua, o que daria 2 litros a menos no balde B 
		Despejar(baldeB em baldeA);	
	enquanto balde C não estiver cheio:	//Enchendo balde C de agua, o que daria 4 litros a menos no balde B 
		Despejar(baldeB em baldeC);	//tendo o balde B 7 litros no começo, 7-2(baldeA)-4(baldeC)=1 Litro restante 
	Saida(baldeB);```