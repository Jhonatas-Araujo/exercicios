contador = 1
soma = media = 0

while contador <=10:
    num = float(input("Digite um numero: "))
    if num >= 0:
        soma = soma + num
        contador += 1
    else:
        print("valor negativo não é aceito. Tente novamente.")

media = soma/10
print(f"A soma é {soma}")
print(f"A média é {media}")