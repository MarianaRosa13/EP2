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
    grade+=NUMEROS[i] + '\n'     #TEM QUE ARRUMAR O 10!!!!!!!!
    i+=1
print(grade)

posicao_letra=input('Informe a letra:').upper()
while posicao_letra not in cabecalho:
    print('Posição inválida')
    posicao_letra=input('Informe a letra:').upper()
posicao_num=input('Informe o número:')
if posicao_num not in grade:
    print('Posição inválida')
    posicao_num=input('Informe o número:')
orient=input('Informe a orientação: [v/h]')
posicao_stg=posicao_letra + posicao_num
print(posicao_stg)
num_linha=int(posicao_num)

for l in range(len(ALFABETO)):
   if ALFABETO[l]==posicao_letra:
      num_coluna=l
print(num_coluna)

print('Ainda falta: '+', '.join(lista_frota))

print(cabecalho) 

mapa=cria_mapa(n)

# for arma in lista_frota:
#   if posicao_suporta(mapa,quant,posicao_num,posicao_letra,orient)==True:
#     for pos in mapa:
#       if pos=='N':
#         pos='\u001b[33m▓'

print('Iniciando batalha naval!')
time.sleep(1)
i=5
while i!=0:
    print(i)
    time.sleep(1)
    i-=1



letra_atq=input('Digite a letra:')
coluna_atq=0
for l in range(len(ALFABETO)):
   if ALFABETO[l]==letra_atq:
      coluna_atq=l
num_atq=int(input('Digite o número:'))
posicao_atq=mapa[num_atq][coluna_atq]
print(posicao_atq)
if posicao_atq=='N':
  print(f'Jogador --->>>{posicao_atq}')
  print('BOOOMMM!!')
  posicao_atq='\u001b[31m▓'
else:
  print(f'Jogador --->>>{posicao_atq}')
  print('Água!')
  posicao_atq='\u001b[34m▓'
print(mapa)
#print(mapa_comp)


#criar um dicionario com as posicoes em que há navioes depois de alocar
#se a posicao estiver no dicionario: boomm, senao: agua


if foi_derrotado(mapa)==True:
    print('Você perdeu!')
    print('O computador ainda é o senhor dos mares!')
    novamente=input('Jogar novamente? [s/n]')


# if foi_derrotado(mapa)==True:
#     print('Você venceu!')
#     print('Temos um novo cherife nos mares!')
#     print('Jogar novamente? [s/n]')
# else:
#     print('Você perdeu!')
#     print('O computador ainda é o senhor dos mares!')
#     print('Jogar novamente? [s/n]')