cont = 0
linha = int(input("Digite a quantidade de linhas da matriz \t"))
coluna = int(input("Digite a quantidade de colunas da matriz \t"))
matriz = [0] * linha

for l in range(len(matriz)):
    matriz[l] = [0]
    print(matriz[l])

    tam = linha*coluna
    vetor_val = [None] * tam

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = int(input("Digite o valor \t"))
    if matriz[l][c] > 10:
        vetor_val[cont] = matriz[l][c]
        cont = cont+1
    print(matriz[l])

for l in range(len(matriz)):
    print(matriz[l])

print(vetor_val)
print(cont)
print("")