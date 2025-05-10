#Exercício de fixação 8: Crie um programa que solicite ao usuário as quatro notas bimestrais de uma matéria e o número de faltas. Informe se o aluno foi aprovado ou reprovado, bem como o motivo, a saber:
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))
faltas = int(input("Quantas vezes você faltou: "))

median = (nota1 + nota2 + nota3 + nota4) / 4
print("Sua média na disciplina foi", median)

mediaf = 100 - (faltas * 100) / 40
print("Sua quantidade de faltas foi", mediaf, "%")

if median >= 7 and mediaf >= 75:
    print("Você está aprovado!")
elif median >= 7 and mediaf < 75:
    print("Você está reprovado por faltas.")
elif median < 7 and mediaf >= 75:
    print("Você está reprovado por nota.")
else:
    print("Você está reprovado por notas e por faltas")