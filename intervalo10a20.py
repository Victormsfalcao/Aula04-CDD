qtdDentro = 0
qtdFora = 0
for i in range (0,10):
    num = int(input("Insira um número: "))
    if num >= 10 and num <= 20:
        qtdDentro +=1
    else:
        qtdFora +=1
print(f"A quantidade de números entre 10 e 20 é {qtdDentro} e a quantidade de numeros fora desse intervalo é {qtdFora} ! ")
