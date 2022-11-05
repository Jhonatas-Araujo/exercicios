from random import randint
chave_pesquisa = 0
achou = 0
pos_linha= 0 
pos_coluna = 0

linha = int(input("Digite a quantidade de linhas da matriz \t"))
coluna = int(input("Digite a quantidade de colunas da matriz \t"))
matriz = [0] * linha

for l in range(len(matriz)):
    matriz[l] = [0] * coluna

chave_pesquisa = int(input("Digite um valor de pesquisa: "))

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = randint(0,100)
        if matriz[l][c] == chave_pesquisa:
            pos_linha = l
            pos_coluna = c
            achou = 1

for l in range(len(matriz)):
    print(matriz[l])

if achou == 1:
    print("O valor pesquisado esta na linha, ", pos_linha, " e na coluna, ", pos_coluna)
else:
    print("Valor nao encontrado")