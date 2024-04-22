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

print(cria_mapa(10))