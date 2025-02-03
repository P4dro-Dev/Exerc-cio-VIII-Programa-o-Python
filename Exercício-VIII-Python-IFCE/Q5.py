def calcular_valor_total():
    """
    Calcula o valor total a pagar de uma compra, considerando a forma de pagamento.
    """

    try:
        valor_compra = float(input("Digite o valor da compra: "))
    except ValueError:
        print("Valor da compra inválido. Digite um número.")
        return

    forma_pagamento = input("Digite a forma de pagamento (À vista, Parcelado ou Outro): ").lower()

    if forma_pagamento == "à vista":
        valor_total = valor_compra * 0.9  # 10% de desconto
        print(f"Total = R$ {valor_total:.2f}")
    elif forma_pagamento == "parcelado":
        try:
            parcelas = int(input("Digite a quantidade de parcelas: "))
        except ValueError:
            print("Quantidade de parcelas inválida. Digite um número inteiro.")
            return

        if parcelas <= 2:
            valor_total = valor_compra
        elif parcelas >= 3:
            valor_total = valor_compra * 1.15  # 15% de juros
        else:
            print("Quantidade de parcelas inválida.")
            return
        print(f"Total = R$ {valor_total:.2f}")
    else:
        print("Forma de pagamento inválida.")

calcular_valor_total()