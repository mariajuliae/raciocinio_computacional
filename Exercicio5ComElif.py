print("Por favor, insira três números diferented: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

#verificando se os números são diferentes
if num1 == num2:
    print("Os números inseridos não são diferentes.")
elif num1 == num3:
        print("Os números inseridos não são diferentes.")
elif num2 == num3:
            print("Os números inseridos não são diferentes.")
else:
    if num1 < num2:
        if num1 < num3:
            print("O menor número é:", num1)
        else:
            print("O menor número é:", num3)

    elif num2 < num3:
        print("O menor número é:", num2)
    else:
        print("O menor número é:", num3)