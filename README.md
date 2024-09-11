## Estagio_RB
 
> Respostas 
 ## 3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA); 
+ Soma = 77.

## 4) Descubra a lógica e complete o próximo elemento:
+ a) 1, 3, 5, 7,....9 
+ 2, 4, 8, 16, 32, 64,....128
+ 0, 1, 4, 9, 16, 25, 36,....49
+ 4, 16, 36, 64,....100
+ 1, 1, 2, 3, 5, 8,....13
+ 2,10, 12, 16, 17, 18, 19,....20

## 5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada? 

Identificar e marcar os interruptores:

 Nomear os interruptores como A, B e C.
 
  + Primeira ação:
  
        Ligar o interruptor A e deixar ligado por um período de tempo razoável (por exemplo, 10-15 minutos);
   
        Após o tempo, desligar o interruptor A e ligar o interruptor B;
   
   Deixar o interruptor B ligado e manter o interruptor C desligado.
   
 + Primeira ida às salas das lâmpadas:
  
       Observar o estado de cada lâmpada.
   
       Identificação das lâmpadas:

Lâmpada 1:

    Se estiver acesa, então ela é controlada pelo interruptor B (pois está ligada no momento).

Lâmpada 2:

    Se estiver apagada e quente, então ela é controlada pelo interruptor A (pois estava ligada anteriormente e ainda mantém calor).

Lâmpada 3:

    Se estiver apagada e fria, então ela é controlada pelo interruptor C (pois nunca foi ligada).


+ Resumo:
  
    Lâmpada acesa: Controle pelo interruptor B (porque está ligada no momento da sua visita).
    Lâmpada apagada e quente: Controle pelo interruptor A (porque estava ligada anteriormente e ainda mantém calor).
    Lâmpada apagada e fria: Controle pelo interruptor C (porque nunca foi ligada).
