num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
op = input("Qual operação você deseja utilizar (+ - * /)? ")
result = 0
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1/num2
else:
    op = "erro"
if op == "erro":
    print("Operação inválida!)")
else:
    print(print(num1,op,num2, "=", result))
