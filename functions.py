#função que cria o mapa
from constants import *

def cria_mapa(n):
    matriz=[]
    for _ in range(n):
        linha_nova=[]
        for _ in range(n):
            linha_nova.append('   ')
        matriz.append(linha_nova)
    return matriz

# função que define se o jogador perdeu
def foi_derrotado(matriz):
    N=u"\u001b[43m  \u001b[0m "
    for i in range(len(matriz)):
        linha=matriz[i]
        for j in range(len(linha)):
            if linha[j]== N :
                return False
    return True

# função que define se a posição é válida
def posicao_suporta(mapa,num,num_linha,pos_letra,orient):
    N=u"\u001b[41m  \u001b[0m "
    linha=mapa[num_linha-1]
    if orient=='h':
        if len(linha)-pos_letra<num:
            return False
        if linha[pos_letra]== N:
            return False
        else:
            for i in range(0,num):
                if mapa[num_linha-1][pos_letra+i]== N:
                    return False
    elif orient=='v':
        if len(mapa)-num_linha<num:
            return False
        if linha[pos_letra]== N:
            return False
        else:
            for i in range(0,num):
                if mapa[num_linha+i][pos_letra]== N:
                    return False
    return True

# função que aloca os navios
import random
def aloca_navios(mapa,lista):
    X=u"\u001b[41m  \u001b[0m "
    for quant in lista:
        linha=random.randint(0, quant-1)
        coluna=random.randint(0, quant-1)
        orientacao=random.choice(['h', 'v'])
        while posicao_suporta(mapa,quant,linha,coluna,orientacao)==False:
            linha=random.randint(0, quant-1)
            coluna=random.randint(0, quant-1)
            orientacao=random.choice(['h', 'v'])
        for i in range(0,quant):
            if orientacao=='h':
                mapa[linha][coluna+i]=X
            elif orientacao=='v':
                mapa[linha+i][coluna]=X           
    return mapa

#função que imprime o mapa 
def imprime_mapa(m):
    dim = len(m)
    letras=ALFABETO[:dim]
    cabecalho=''
    for i in letras:
        if i=='A':
            cabecalho+='  '+ i + ' '
        else:
            cabecalho+=' '+ i + ' '
    print(cabecalho)
    for lin in range(dim):
        linha = f'{lin+1} '
        for col in range(dim):
            linha += m[lin][col]
        linha += f'{lin+1} '
        print(linha)