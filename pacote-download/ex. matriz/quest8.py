
linha = int(input("Digite a quantidade de linhas da matriz \t"))
coluna = int(input("Digite a quantidade de colunas da matriz \t"))
matriz = [0] * linha

for l in range(len(matriz)):
    matriz[l] = [0] * coluna
    
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if l == c:
            matriz[l][c] = 1
        else:
            matriz[l][c] = 0
        
for l in range(len(matriz)):
    print(matriz[l])

