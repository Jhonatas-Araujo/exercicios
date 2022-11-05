from random import randint
soma = 0
chave = 0
pos_linha = 0
pos_coluna = 0
linha = int(input("Digite a quantidade de linhas da matriz \t"))
coluna = int(input("Digite a quantidade de colunas da matriz \t"))
matriz = [0] * linha

for l in range(len(matriz)):
    matriz[l] = [0] * coluna
chave = int(input("Digite um valor: \t"))    
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = int(input("Digite um valor: \t"))
        if matriz[l][c] == chave:
            pos_linha = l
            pos_coluna = c
            achou = 1
            
            
for l in range(len(matriz)):
    print(matriz[l])
    
print("linha: ",pos_linha)
print("coluna: ",pos_coluna)

