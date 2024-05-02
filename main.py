#importa as outras páginas
from constants import *
from functions import *
import time


#variável que decide se o jogo recomeça
jogo=True
#enquanto quiser jogar, o jogo recomeça
while jogo==True:
  #faz a introdução do jogo
  print('=====================================================')
  print('Bem vindo ao melhor jogo de Batalha Naval do Insper!')
  print('=====================================================')
  time.sleep(1)
  print('Seu jogo está começando...')
  time.sleep(1)
  print('Escolha um país para defender:')
  #faz a string dos países
  paises_stg=''
  i=1
  for pais,frota in PAISES.items():
    i_stg=str(i)
    paises_stg+=i_stg + ': '
    paises_stg+=pais + '\n'
    for arma,qtd in frota.items():
      paises_stg+= '   '
      qtd_stg=str(qtd)
      paises_stg+=qtd_stg + ' ' + arma
      paises_stg+='\n'
    i+=1
  print(paises_stg)

  #pede o numero do país para o usuário
  num_pais=int(input('Qual é o número da nação da sua frota?'))
  #printa a nação escolhida
  seu_pais=lista_paises[num_pais-1]
  print(f'Você escolheu a nação {seu_pais}')
  #pede o tamanho do tabuleiro
  n=int(input('Qual é o tamanho do seu tabuleiro?'))

  #sorteia um país para o computador
  num_sorteado=random.randint(0,len(lista_paises)-1)
  pais_sorteado=lista_paises[num_sorteado]
  while pais_sorteado == seu_pais:
    num_sorteado=random.randint(0,len(lista_paises)-1)
    pais_sorteado=lista_paises[num_sorteado]
  print(f'O computador é: {pais_sorteado}')

  print('Agora é a sua vez de alocar seus navios de guerra!')

  #mostra o mapa do tamanho escolhido para o usuário
  mapa=cria_mapa(n)
  imprime_mapa(mapa)

  #coloca os navios do país na lista da frota
  dicio=PAISES[lista_paises[num_pais-1]]
  lista_frota=[]
  for navio,quant in dicio.items():
      for i in range(quant):
          lista_frota.append(navio)

  #faz um cabeçalho para o tabuleiro
  cabecalho='  '
  letras=ALFABETO[:n]
  for i in letras:
    cabecalho+='  '+ i + '  '

  #printa a lista de navios
  print('Seus navios: '+', '.join(lista_frota))

 #variável da cor amarela
  N= u"\u001b[33m▓  \u001b[0m"

  #para cada tipo de navio mostrar o tipo de navio a ser alocado
  for arma in lista_frota:
    print(f'Hora de alocar: {arma}')
  #pedir a letra para alocar,formatar como maiúscula,ver se a letra está no cabeçalho
    posicao_letra=input('Informe a letra:').upper()
    while posicao_letra not in cabecalho:
        print('Posição inválida')
        posicao_letra=input('Informe a letra:').upper()
    #pedir o número, verificar se o número está no tamanho do mapa
    posicao_num=input('Informe o número:')
    num_linha=int(posicao_num)
    while num_linha>len(mapa):
        print('Posição inválida')
        posicao_num=input('Informe o número:')
    #pedir a orientação
    orient=input('Informe a orientação: [v/h]')
    while orient!='v' and orient!='h':
      print('Orientação inválida')
      orient=input('Informe a orientação: [v/h]')
    #fazer uma string da posição
    posicao_stg=posicao_letra + posicao_num
    #achar o numero da coluna a partir da letra
    for l in range(len(ALFABETO)):
        if ALFABETO[l]==posicao_letra:
          num_coluna=l
    #achar o tamanho do navio
    for navio,quant in CONFIGURACAO.items():
        if arma in CONFIGURACAO.keys():
          quant=CONFIGURACAO[arma]
    #enquanto não puder alocar, dá inválido, pergunta de novo, e pega a posição de novo
    while posicao_suporta(mapa,quant,num_linha,num_coluna,orient)==False:
        print('Local inválido')
        posicao_letra=input('Informe a letra:').upper()
        while posicao_letra not in cabecalho:
          print('Posição inválida')
          posicao_letra=input('Informe a letra:').upper()
        for l in range(len(ALFABETO)):
          if ALFABETO[l]==posicao_letra:
            num_coluna=l
        posicao_num=input('Informe o número:')
        while num_linha>len(mapa):
          print('Posição inválida')
          posicao_num=input('Informe o número:')
        orient=input('Informe a orientação: [v/h]')
    #se der para alocar, aloca na vertical ou horizontal até acabar a quantidade
    if posicao_suporta(mapa,quant,num_linha,num_coluna,orient)==True:
        for i in range(0,quant):
          if orient=='h':
              mapa[num_linha-1][num_coluna+i] = N
          elif orient=='v':
              if num_linha>=9:
                mapa[num_linha-1+i][num_coluna] = N
              else:
                mapa[num_linha-1+i][num_coluna] = N
          imprime_mapa(mapa)
   
  #começa a batalha naval
  print('Iniciando batalha naval!')
  #faz a contagem regressiva
  time.sleep(1)
  i=5
  while i!=0:
      print(i)
      time.sleep(1)
      i-=1
  print('Hora de atacar!')
  time.sleep(1)

  print(mapa)

  #cria um mapa em branco
  mapa_comp_branco=cria_mapa(n)
  mapa_c=cria_mapa(n)
  #pega o armamento do país do computador
  muni=PAISES[pais_sorteado]
  lista_aloc=[]
  #coloca na lista a quantidade das armas do país do computador
  for arma, quant in muni.items():
    if arma in CONFIGURACAO:
        while quant!=0:
          lista_aloc.append(CONFIGURACAO[arma])
          quant-=1

  #faz um mapa alocando os navios da lista
  mapa_comp=aloca_navios(mapa_c,lista_aloc)

   #variável com a cor azul
  A=u"\u001b[34m▓  \u001b[0m"
   #variável com a cor vermelha
  X=u"\u001b[31m▓  \u001b[0m"

  #cria duas listas para as posições que já foram atacadas do jogador e computador
  lista_atacados=[]
  lista_posicoes=[]
  #executa o código de ataque enquanto ninguém ganhou
  while foi_derrotado(mapa)==False and perdeu(mapa_comp)==False:
      #mostra os mapas
      print(f'Computador: {pais_sorteado}')
      imprime_mapa(mapa_comp_branco)
      print(f'Jogador: {seu_pais}')
      imprime_mapa(mapa)
      #pergunta a letra de ataque e verifica se é válida
      letra_atq=input('Digite a letra:').upper()
      while letra_atq not in cabecalho:
         print('Posição inválida')
         letra_atq=input('Digite a letra:').upper()
      coluna_atq=0
      #acha a coluna a partir da letra
      for l in range(len(ALFABETO)):
         if ALFABETO[l]==letra_atq:
            coluna_atq=l
      #pergunta a linha de ataque e verifica se é válida
      num_atq=int(input('Digite o número:'))
      while num_atq>len(mapa):
         print('Posição inválida')
         posicao_num=input('Digite o número:')
      #faz a string da posição
      num_atq_stg=str(num_atq)
      posicao_atq = mapa_comp[num_atq-1][coluna_atq]
      posicao_atq_stg=letra_atq + num_atq_stg
      #se a posição ainda não foi atacada
      if posicao_atq_stg not in lista_atacados:
        #coloca ela na lista de lugares atacados
        lista_atacados.append(posicao_atq_stg)
        print(lista_atacados)
        #verifica se tem barco na posição, se é boomm ou água
        print('posicao atacada do jogador:',posicao_atq)
        print('lista de atacados:',lista_atacados)
        if posicao_atq==X:
          print(f'Jogador --->>>{posicao_atq_stg}')
          mapa_comp_branco[num_atq-1][coluna_atq] = X
          mapa_comp[num_atq-1][coluna_atq] = N
          print('BOOOMMM!!')
        else:
          print(f'Jogador --->>>{posicao_atq_stg}')
          mapa_comp_branco[num_atq-1][coluna_atq] = A
          print('Água!')
      else:
        print('Você já atacou essa posição')
        continue

      #sorteia posição para o computador atacar
      lincomp_atq=random.randint(0,len(mapa)-1)
      colcomp_atq=random.randint(0,len(mapa)-1)
      lincomp_stg=str(lincomp_atq+1)
      letra_atq_comp=''
      #pega a letra a partir da coluna sorteada
      for l in range(len(ALFABETO)):
         letra_atq_comp=ALFABETO[colcomp_atq]
      comp_atq=mapa[lincomp_atq][colcomp_atq]
      print(f'Linha: {lincomp_atq}')
      print(f'Coluna: {colcomp_atq}')
      #faz string da posição
      comp_atq_stg=letra_atq_comp + lincomp_stg
      #verifica se a posição já está na lista das posições atacadas
      #se não estiver na lista, coloca na lista e ataca
      print('lista onde o pc atacou:',comp_atq_stg)
      print('lista do computador atacado:',lista_posicoes)
      if comp_atq_stg not in lista_posicoes:
         lista_posicoes.append(comp_atq_stg)
         print(f'esse é o n: {N}')
         print(f'esse é o ataque: {comp_atq}')
         #verifica se tem barco ou não
         if comp_atq == N:
            mapa[lincomp_atq][colcomp_atq] = X
            print(f'Computador --->>>{comp_atq_stg}')
            print('BOOOMMM!!')
         else:
            mapa[lincomp_atq][colcomp_atq] = A
            print(f'Computador --->>>{comp_atq_stg}')
            print('Água!')
      #se estiver na lista, sorteia outros números para as posições
      else:
         print('ta na listaaaaa')
         while comp_atq_stg in lista_posicoes:
            print('ainda na lista')
            lincomp_atq=random.randint(0,len(mapa)-1)
            colcomp_atq=random.randint(0,len(mapa)-1)
            lincomp_stg=str(lincomp_atq+1)
            letra_atq_comp=''
            for l in range(len(ALFABETO)):
               letra_atq_comp=ALFABETO[colcomp_atq]
            comp_atq=mapa[lincomp_atq-1][colcomp_atq]
            comp_atq_stg=letra_atq_comp + lincomp_stg
            print(f'Linha: {lincomp_atq}')
            print(f'Coluna: {colcomp_atq}')
            print(f'posição nova: {comp_atq_stg}')

  #se o jogador perdeu, avisa que perdeu e pergunta se quer recomeçar o jogo
  if foi_derrotado(mapa)==True:
    print('Você perdeu!')
    print('O computador ainda é o senhor dos mares!')
    novamente=input('Jogar novamente? [s/n]')
    #se quiser recomeçar
    if novamente=='s':
      jogo=True
      print('Recomeçando jogo...')
      time.sleep(1)
    #se não quiser recomeçar
    elif novamente=='n':
      jogo=False
      print('Até a próxima!')
    else:
      #se a resposta é inválida, pergunta de novo até ser válida
      while novamente!='s' and novamente!='n':
        print('Inválido')
        novamente=input('Jogar novamente? [s/n]')
      if novamente=='s':
        jogo=True
        print('Recomeçando jogo...')
        time.sleep(1)
      elif novamente=='n':
        jogo=False
        print('Até a próxima!')
  #se o jogador ganhou, avisa que ganhou e pergunta se quer recomeçar o jogo
  elif perdeu(mapa_comp)==True:
    print('Você ganhou!')
    print('Temos um novo senhor dos mares!')
    novamente=input('Jogar novamente? [s/n]')
    #se quiser recomeçar
    if novamente=='s':
      jogo=True
      print('Recomeçando jogo...')
      time.sleep(1)
    #se não quiser recomeçar
    elif novamente=='n':
      jogo=False
      print('Até a próxima!')
    else:
      #se a resposta é inválida, pergunta de novo até ser válida
      while novamente!='s' and novamente!='n':
        print('Inválido')
        novamente=input('Jogar novamente? [s/n]')
      if novamente=='s':
        jogo=True
        print('Recomeçando jogo...')
        time.sleep(1)
      elif novamente=='n':
        jogo=False
        print('Até a próxima!')