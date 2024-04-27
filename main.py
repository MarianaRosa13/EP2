from constants import *
from functions import *
import time

# paises_stg=''
# i=0
# for pais,frota in PAISES.items():
#    paises_stg+='1'
#    paises_stg+=': '
#    paises_stg+=pais + '\n'
#    for arma,qtd in frota:
#       paises_stg+=qtd + frota
#    i+=1
print(PAISES)
#print(paises_stg)
num_pais=int(input('Qual é o número da nação da sua frota?'))
print(f'Você escolheu a nação {lista_paises[num_pais-1]}')
n=int(input('Qual é o tamanho do seu tabuleiro?'))
print('Agora é a sua vez de alocar seus navios de guerra!')

mapa=cria_mapa(n)
print(mapa)

dicio=PAISES[lista_paises[num_pais-1]]
lista_frota=[]
for navio,quant in dicio.items():
    for i in range(quant):
        lista_frota.append(navio)

cabecalho='  '
letras=ALFABETO[:n]
for i in letras:
   cabecalho+='  '+ i + '  '

grade=''
i=0
while i<=n:
    if i==NUMEROS[-2]:
       grade+=NUMEROS[i]+NUMEROS[i+1]
    else:
        grade+=NUMEROS[i] + '\n'
    i+=1


# print(' '+ cabecalho + ' ')
# for i in mapa:
#    linha_branco=str(i)
#    print(grade[i+1] + linha_branco + grade[i+1])  #TA DANDO PROBLEMA NO I+1!!!!!!!!!! not convert to list


# posicao_letra=input('Informe a letra:').upper()
# while posicao_letra not in cabecalho:
#     print('Posição inválida')
#     posicao_letra=input('Informe a letra:').upper()
# posicao_num=input('Informe o número:')
# if posicao_num not in grade:
#     print('Posição inválida')
#     posicao_num=input('Informe o número:')        COLOQUEI ESSE CODIGO DENTRO DO FOR NA LINHA 65!!!!!!!!!!!
# orient=input('Informe a orientação: [v/h]')       TEM QUE TESTAR ELE NO FOR!!!!!!!!!!
# posicao_stg=posicao_letra + posicao_num
# print(posicao_stg)
# num_linha=int(posicao_num)
# for l in range(len(ALFABETO)):
#    if ALFABETO[l]==posicao_letra:
#       num_coluna=l
# print(num_coluna)

print('Ainda falta: '+', '.join(lista_frota))



for arma in lista_frota:
  for navio,quant in dicio.items():
     print(lista_frota)
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
     for navio,quant in dicio.items():    #ELE TA PASSANDO OS NAVIOS MAIS RAPIDO DO QUE ALOCA!!!!!!!!
        if posicao_suporta(mapa,quant,num_linha,num_coluna,orient)==True:
           print('entrouuuuuuu')
           print(navio)
           imprime_mapa(mapa)
           for i in range(0,quant):
            if orient=='h':
               mapa[num_linha-1][num_coluna+i]=' N '
            elif orient=='v':
               mapa[num_linha-1+i][num_coluna]=' N '
            imprime_mapa(mapa)
            del lista_frota[lista_frota.index(navio)]
            print('Ainda falta: '+', '.join(lista_frota))
        # else:
        #    continue


for pos in mapa:
    if pos==' N ':
        pos='\u001b[33m▓'
            #print(pos)
imprime_mapa(mapa)



print('Iniciando batalha naval!')
time.sleep(1)
i=5
while i!=0:
    print(i)
    #time.sleep(1)
    i-=1



letra_atq=input('Digite a letra:')
coluna_atq=0
for l in range(len(ALFABETO)):
   if ALFABETO[l]==letra_atq:
      coluna_atq=l
num_atq=int(input('Digite o número:'))
posicao_atq=mapa[num_atq][coluna_atq]
print(posicao_atq)
if posicao_atq==' N ':
  print(f'Jogador --->>>{posicao_atq}')
  print('BOOOMMM!!')
  posicao_atq='\u001b[31m▓'
else:
  print(f'Jogador --->>>{posicao_atq}')
  print('Água!')
  posicao_atq='\u001b[34m▓'
imprime_mapa(mapa)
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