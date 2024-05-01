#imports
from constants import *
from functions import *
import time

#novamente='s'
#while novamente=='s':

#faz a string dos países
paises_stg=''
i=1
for pais,frota in PAISES.items():
  i_stg=str(i)
  paises_stg+=i_stg + ': '
  paises_stg+=pais + '\n'
  for arma,qtd in frota.items():
    qtd_stg=str(qtd)
    paises_stg+=qtd_stg + ' ' + arma + ' '
  paises_stg+='\n'
  i+=1
print(PAISES)
print(paises_stg)

#pede o numero do país para o usuário
num_pais=int(input('Qual é o número da nação da sua frota?'))
#printa a nação escolhida 
seu_pais=lista_paises[num_pais-1]
print(f'Você escolheu a nação {seu_pais}')
#pede o tamanho do tabuleiro
n=int(input('Qual é o tamanho do seu tabuleiro?'))
print('Agora é a sua vez de alocar seus navios de guerra!')

#sorteia um país para o computador
num_sorteado=random.randint(0,len(lista_paises)-1)
pais_sorteado=lista_paises[num_sorteado]
print(f'O computador é: {pais_sorteado}')


#mostra o mapa do tamanho escolhido para o usuário
mapa=cria_mapa(n)
print(mapa)

#lista_mapas=[mapa_comp,mapa]


#coloca o tipo de navio na lista da frota
dicio=PAISES[lista_paises[num_pais-1]]
lista_frota=[]
for navio,quant in dicio.items():
    for i in range(quant):
        lista_frota.append(navio)

#define um cabeçalho
cabecalho='  '
letras=ALFABETO[:n]
for i in letras:
   cabecalho+='  '+ i + '  '


#printa a lista de navios
print('Seus navios: '+', '.join(lista_frota))

N=u"\u001b[43m  \u001b[0m "

#para cada tipo de navio mostrar o tipo de navio a ser alocado
for arma in lista_frota:
   print(lista_frota)
   print(f'Hora de alocar: {arma}')
#pedir a letra para alocar,formatar como maiúscula,ver se a letra está no cabeçalho
   posicao_letra=input('Informe a letra:').upper()         #ISSO
   while posicao_letra not in cabecalho:
      print('Posição inválida')
      posicao_letra=input('Informe a letra:').upper()    #TA
   #pedir o número, verificar se o número está no tamanho do mapa
   posicao_num=input('Informe o número:')
   num_linha=int(posicao_num)
   while num_linha>len(mapa):
      print('Posição inválida')
      posicao_num=input('Informe o número:')            #FUNCIONANDO!!!!!!!!!!
   #pedir orientação
   orient=input('Informe a orientação: [v/h]')
   posicao_stg=posicao_letra + posicao_num
   print(posicao_stg)
   print(len(mapa))
   print(f'Linha: {num_linha}')
   for l in range(len(ALFABETO)):
      if ALFABETO[l]==posicao_letra:
         num_coluna=l
   print(f'Coluna: {num_coluna}')
   #colocar o tamanho dos navios 
   for navio,quant in CONFIGURACAO.items():
      print(arma)
      if arma in CONFIGURACAO.keys():
         quant=CONFIGURACAO[arma]
      print(f'Quantidade: {quant}')
   while posicao_suporta(mapa,quant,num_linha,num_coluna,orient)==False:
      print('Local inválido')
      posicao_letra=input('Informe a letra:').upper()         #ISSO
      while posicao_letra not in cabecalho:
         print('Posição inválida')
         posicao_letra=input('Informe a letra:').upper()    #TA
      posicao_num=input('Informe o número:')
      while num_linha>len(mapa):
         print('Posição inválida')
         posicao_num=input('Informe o número:')            #FUNCIONANDO!!!!!!!!!!
      orient=input('Informe a orientação: [v/h]')
   if posicao_suporta(mapa,quant,num_linha,num_coluna,orient)==True:
      print('entrouuuu')
      for i in range(0,quant):
         if orient=='h':
            mapa[num_linha-1][num_coluna+i] = N
         elif orient=='v':
            if num_linha>=9:
               mapa[num_linha-1+i][num_coluna] = N
            else:
               mapa[num_linha-1+i][num_coluna] = N
         #colocar o for pos in mapa aqui!!!!!!!!! 
         '''for pos in mapa:
            if pos== N:
               pos=u"\u001b[43m  \u001b[0m "'''
            #print(pos)
         imprime_mapa(mapa)   
         #del lista_frota[lista_frota.index(arma)]      #TA DANDO QUE NAO EXISTE
         print('Ainda falta: '+', '.join(lista_frota))

'''for pos in mapa:
    if pos==' N ':
        pos=u"\u001b[41m  \u001b[0m "
            #print(pos)
imprime_mapa(mapa)

#mapa
for pos in mapa:
    for h in range(len(pos)):
        if pos[h]==' N ':
            pos.remove(' N ')
            pos.insert(h, u"\u001b[41m  \u001b[0m ")
            mapa=' '.join(pos)
print(mapa)  '''



print('Iniciando batalha naval!')
time.sleep(1)
i=5
while i!=0:
    print(i)
    #time.sleep(1)
    i-=1

mapa_comp_branco=cria_mapa(n)
mapa_c=cria_mapa(n)
muni=PAISES[pais_sorteado]
lista_aloc=[]
for arma, quant in muni.items():
   if arma in CONFIGURACAO:
      while quant!=0:
         lista_aloc.append(CONFIGURACAO[arma])
         quant-=1
print(lista_aloc)

mapa_comp=aloca_navios(mapa_c,lista_aloc)
print(mapa_comp)


A=u"\u001b[44m  \u001b[0m "
print(N)
print(A)
X=u"\u001b[41m  \u001b[0m "
print(X)


#lista_mapas=[mapa_comp,mapa]
while foi_derrotado(mapa)==False: 
   imprime_mapa(mapa_comp)
   imprime_mapa(mapa_comp_branco)
   imprime_mapa(mapa)
   letra_atq=input('Digite a letra:').upper()
   while letra_atq not in cabecalho:
      print('Posição inválida')
      letra_atq=input('Digite a letra:').upper()
   coluna_atq=0
   for l in range(len(ALFABETO)):
      if ALFABETO[l]==letra_atq:
         coluna_atq=l
   print(f'Coluna: {coluna_atq}')
   num_atq=int(input('Digite o número:'))
   while num_atq>len(mapa):
      print('Posição inválida')
      posicao_num=input('Digite o número:')
   print(f'Linha: {num_atq}')
   num_atq_stg=str(num_atq)
   posicao_atq = mapa_comp[num_atq-1][coluna_atq]
   print(mapa_comp[num_atq-1][coluna_atq])
   print(f'Posicao comp: {posicao_atq}')
   print(f'Posicao branco: {mapa_comp_branco[num_atq-1][coluna_atq]}') 
   posicao_atq_stg=letra_atq + num_atq_stg
   if posicao_atq==X:
      print(f'Jogador --->>>{posicao_atq_stg}')
      mapa_comp_branco[num_atq-1][coluna_atq] = X 
      print('BOOOMMM!!')
   else:
      print(f'Jogador --->>>{posicao_atq_stg}')
      mapa_comp_branco[num_atq-1][coluna_atq] = A
      print('Água!')

if foi_derrotado(mapa)==True:
   print('Você perdeu!')
   print('O computador ainda é o senhor dos mares!')
   novamente=input('Jogar novamente? [s/n]')
   if novamente=='s':
      print('recomeça')  #restart
   else:
      print('acaba') #para tudo