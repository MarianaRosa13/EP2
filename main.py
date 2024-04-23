from constants import *
from functions import *
import time

print(PAISES)
num_pais=int(input('Qual é o número da nação da sua frota?'))
print(f'Você escolheu a nação {lista_paises[num_pais-1]}')
n=int(input('Qual é o tamanho do seu tabuleiro?'))
print('Agora é a sua vez de alocar seus navios de guerra!')

dicio=PAISES[lista_paises[num_pais-1]]
lista_frota=[]
for navio,quant in dicio.items():
    for i in range(quant):
        lista_frota.append(navio)


letras=ALFABETO[:n]
cabecalho=''
for i in letras:
    cabecalho+=' '+ i + ' '

grade=''
i=0
while i<=n:
    grade+=NUMEROS[i]
    i+=1

posicao_letra=input('Informe a letra:').upper()
while posicao_letra not in cabecalho:
    print('Posição inválida')
    posicao_letra=input('Informe a letra:').upper()
posicao_num=input('Informe o número:')
if posicao_num not in grade:
    print('Posição inválida')
    posicao_num=input('Informe o número:')
posicao=posicao_letra + posicao_num
print(posicao)

print(cabecalho) 


#for arma in lista_frota:
    #aloca
    # if arma=='cruzador':
    #     print('▓'*2)
    # if arma=='porta-avioes':
    #     print('▓'*5)
    # if arma=='couracado':
    #     print('▓'*4)
    # if arma=='destroyer':
    #     print('▓'*3)
    # if arma=='submarino':
    #     print('▓'*2)
    # if arma=='torpedeiro':
    #     print('▓'*)????????

print('Iniciando batalha naval!')
time.sleep(1)
i=5
while i!=0:
    print(i)
    time.sleep(1)
    i-=1


#criar um dicionario com as posicoes em que há navioes depois de alocar
#se a posicao estiver no dicionario: boomm, senao: agua


#venceu=foi_derrotado(mapa)

# if venceu==True:
#     print('Você venceu!')
#     print('Temos um novo cherife nos mares!')
#     print('Jogar novamente? [s/n]')
# else:
#     print('Você perdeu!')
#     print('O computador ainda é o senhor dos mares!')
#     print('Jogar novamente? [s/n]')