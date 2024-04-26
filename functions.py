def cria_mapa(n):
    matriz=[]
    linha_nova=[]
    while len(linha_nova)<n:
        linha_nova.append(' ')
    while len(matriz)<n:
        matriz.append(linha_nova)
    return matriz

def foi_derrotado(matriz):
    for i in range(len(matriz)):
        linha=matriz[i]
        for j in range(len(linha)):
            if linha[j]=='N':
                return False
    return True

def posicao_suporta(mapa,num,num_linha,pos_letra,orient):
    linha=mapa[num_linha]
    if orient=='h':
        if len(linha)-pos_letra<num:
            return False
        if linha[pos_letra]=='N':
            return False
        else:
            for i in range(0,num):
                if mapa[num_linha][pos_letra+i]=='N':
                    return False
    elif orient=='v':
        if len(mapa)-num_linha<num:
            return False
        if linha[pos_letra]=='N':
            return False
        else:
            for i in range(0,num):
                if mapa[num_linha+i][pos_letra]=='N':
                    return False
    return True

import random
def aloca_navios(mapa,lista):
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
                mapa[linha][coluna+i]='N'
            elif orientacao=='v':
                mapa[linha+i][coluna]='N'            
    return mapa