def verificar_triangulo():
    """
    Verifica se três lados formam um triângulo e, em caso afirmativo,
    classifica o triângulo.
    """

    try:
        lado1 = float(input("Digite o primeiro lado: "))
        lado2 = float(input("Digite o segundo lado: "))
        lado3 = float(input("Digite o terceiro lado: "))
    except ValueError:
        print("Entrada inválida. Digite números para os lados.")
        return

    # Verifica se é possível formar um triângulo
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        if lado1 == lado2 == lado3:
            print("Equilátero")
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("Isósceles")
        else:
            print("Escaleno")
    else:
        print("Não é triângulo")

# Executa a função para verificar e classificar o triângulo
verificar_triangulo()