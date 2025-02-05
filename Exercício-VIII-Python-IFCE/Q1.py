# Desenvolva um programa que leia a classificação indicativa de um filme (número inteiro) e exiba a
# categoria do filme.
#
# Classificação Categoria
# 0 Livre para todos os públicos
# 10 Não recomendado para menores de 10 anos
# 12 Não recomendado para menores de 12 anos
# 14 Não recomendado para menores de 14 anos
# Outros Classificação inválida.


classificacao = int(input("Digite a classificação indicativa do filme: "))

if classificacao == 0:
    print("Livre para todos os públicos")
elif classificacao == 10:
    print("Não recomendado para menores de 10 anos")
elif classificacao == 12:
    print("Não recomendado para menores de 12 anos")
elif classificacao == 14:
    print("Não recomendado para menores de 14 anos")
else:
    print("Classificação inválida")

match classificacao:
    case 0:
        print("Livre para todos os públicos")
    case 10:
        print("Não recomendado para menores de 10 anos")
    case 12:
        print("Não recomendado para menores de 12 anos")
    case 14:
        print("Não recomendado para menores de 14 anos")
    case _:
        print("Classificação inválida")