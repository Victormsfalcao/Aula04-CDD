n = int(input("Insira um número maior que zero: "))

if n < 1:
    print("Incorreto")
    n = int(input("Insira o número: "))
    if n > 0:
        for i in range(1, n + 1, 1):
            print(i, end=" ")
    else:
        print("SEU ANIMAL, TEM QUE SER MAIOR QUE 0")

else:
     for i in range (1,n + 1,1):
         print(i, end=" ")