from random import randint
maior = 0
pos_linha= 0 
pos_coluna = 0

linha = int(input("Digite a quantidade de linhas da matriz \t"))
coluna = int(input("Digite a quantidade de colunas da matriz \t"))
matriz = [0] * linha

for l in range(len(matriz)):
    matriz[l] = [0] * coluna

maior = matriz[0][0]
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = randint(1,100)
        if matriz[l][c] >= maior:
            maior = matriz[l][c]
            pos_linha = l
            pos_coluna = c
for l in range(len(matriz)):
    print(matriz[l])

print("O maior elemento da matriz e ",maior)
print("O elemento esta na linha, ", pos_linha,
    " e na coluna", pos_coluna)