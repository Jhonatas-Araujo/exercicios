from random import randint
somar_impar = 0
soma_col1 = 0 
soma_col2 = 0
soma_col3 = 0

linha = int(input("Digite a quantidade de linhas da matriz \t"))
coluna = int(input("Digite a quantidade de colunas da matriz \t"))
matriz = [0] * linha

for l in range(len(matriz)):
    matriz[l] = [0] * coluna
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = randint(0,50)
        soma_col1 = matriz[0][0] + matriz[1][0] + matriz[2][0] 
        soma_col2 = matriz[0][1] + matriz[1][1] + matriz[2][1] 
        soma_col3 = matriz[0][2] + matriz[1][2] + matriz[2][2] 

        if matriz[l][c] % 2 != 0:
            somar_impar = matriz[l][c] + somar_impar
          

            
        
for l in range(len(matriz)):
    print(matriz[l])

print("Valor da somar impar: ",somar_impar)
print("valor da coluna 1 : ", soma_col1)
print("valor da coluna 1 : ", soma_col2)
print("valor da coluna 1 : ", soma_col3)