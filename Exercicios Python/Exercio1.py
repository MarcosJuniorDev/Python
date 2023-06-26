"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


try:
    valor_int = int(input("Digite o numero inteiro: "))

    if isinstance(valor_int, int):
        if (valor_int % 2) == 0:
            print("Esse numero é par")
        else:
            print("Esse numero é impar")
except:
    print("Esse valor não é inteiro")    