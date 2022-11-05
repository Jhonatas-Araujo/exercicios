maior = menor = 0
vetor = [1,2,4,16,32,64,-128]

for i in range(0,7):
    if vetor[i] == vetor[0]:
        maior = vetor[0]
        menor = vetor[0]
        i = i+1
    else:
        if vetor[i] > maior:
            maior = vetor[i]
        if  vetor[i] < menor:
            menor = vetor[i]
            i = i+1
print('o maior número é: ',maior)
print('o menor número é: ',menor)