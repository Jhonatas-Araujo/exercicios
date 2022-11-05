from random import randint
soma = 0
linha = int(input("Digite a quantidade de linhas da matriz \t"))
coluna = int(input("Digite a quantidade de colunas da matriz \t"))
matriz = [0] * linha

for l in range(len(matriz)):
    matriz[l] = [0] * coluna
    
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = randint(0,100)
        soma = matriz[0][2] + matriz[1][1] + matriz[2][0]    
        
for l in range(len(matriz)):
    print(matriz[l])
    
print("a soma da diagonal secundária é: ",soma)

