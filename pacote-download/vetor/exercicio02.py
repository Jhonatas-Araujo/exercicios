soma = 0 
vetor = [1,2,4,16,32,64,-128]
for i in range(0,7):
    if vetor[i] == vetor[0]:
        soma = vetor[i]
        i +=1
    else:
        soma = vetor[i] + soma
        i +=1
print('a soma é: ',soma)