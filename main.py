from constants import *
from functions import *
import time

print(PAISES)
num_pais=int(input('Qual é o número da nação da sua frota?'))
print(f'Você escolheu a nação {lista_paises[num_pais-1]}')
print('Agora é a sua vez de alocar seus navios de guerra!')

dicio=PAISES[lista_paises[num_pais-1]]
lista_frota=[]
for navio,quant in dicio.items():
    for i in range(quant):
        lista_frota.append(navio)

posicao_letra=input('Informe a letra:')
posicao_num=input('Informe o número:')
posicao=posicao_letra + posicao_num




#for arma in lista_frota:
    #aloca



#quando ganhar: print('Você venceu!') print('Temos um novo cherife nos mares!')