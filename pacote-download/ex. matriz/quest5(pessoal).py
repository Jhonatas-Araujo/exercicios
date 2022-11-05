from random import randint
valorX = 0
pos_l = 0
pos_c = 0
achou = 0

linha = int(input("Digite a quantidade de linhas da matriz \t"))
coluna = int(input("Digite a quantidade de colunas da matriz \t"))
matriz = [0] * linha

for l in range(len(matriz)):
    matriz[l] = [0] * coluna
    
valorX = int(input("Digite o valor procurado: "))
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = randint(1,100)
        if matriz[l][c] == valorX:
            pos_l = l
            pos_c = c
            achou = 1
for l in range(len(matriz)):
    print(matriz[l])

if achou == 1:
    print(f"O valor foi encontrado na posição [{pos_l}][{pos_c}]")
else:
    print("O valor não foi encontrado")