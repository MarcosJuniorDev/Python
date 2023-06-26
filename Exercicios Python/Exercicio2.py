"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

try:
    hora = int(input("Digite a hora: "))

    if hora >= 0 and hora <= 11:
        print("bom dia")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde")
    elif hora > 17 and hora <= 23:
        print("Boa noite")
    else:
        print("hora invalida")
except:
    print("Informe uma hora valida em formato inteiro")