qtd = 0
for i in range (1,11):
    num = int(input("Insira um número:"))
    if num < 0:
        qtd +=1

print(f"A quantidade de números negativos é : {qtd} ! ")

