def gerenciador_notas():
    """
    Gerencia as notas de um estudante, calculando a média e exibindo a situação.
    """

    disciplina = input("Digite o nome da disciplina: ")

    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        nota4 = float(input("Digite a quarta nota: "))
    except ValueError:
        print("Notas inválidas. Digite números.")
        return

    def calcular_media(n1, n2, n3, n4):
        """Calcula a média ponderada das notas."""
        return (n1 * 0.2) + (n2 * 0.2) + (n3 * 0.3) + (n4 * 0.3)

    def exibir_situacao(media):
        """Exibe a situação do aluno com base na média."""
        if media >= 6:
            print("Aprovado")
        elif 3 <= media < 6:
            print("Avaliação Final")
        else:
            print("Reprovado")

    while True:
        print("\nOpções:")
        print("1. Consultar notas")
        print("2. Exibir situação do aluno")
        print("3. Adicionar bonificação")
        print("4. Sair")

        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida. Digite um número.")
            continue

        if opcao == 1:
            media = calcular_media(nota1, nota2, nota3, nota4)
            print(f"Disciplina: {disciplina}")
            print(f"Notas: {nota1}, {nota2}, {nota3}, {nota4}")
            print(f"Média: {media:.2f}")
        elif opcao == 2:
            media = calcular_media(nota1, nota2, nota3, nota4)
            print(f"Média: {media:.2f}")
            exibir_situacao(media)
        elif opcao == 3:
            try:
                bonificacao = float(input("Digite a pontuação de bonificação: "))
                media = calcular_media(nota1, nota2, nota3, nota4)
                media += bonificacao
                print(f"Média atualizada: {media:.2f}")
            except ValueError:
                print("Bonificação inválida. Digite um número.")
        elif opcao == 4:
            break
        else:
            print("Opção inválida.")

# Executa o gerenciador de notas
gerenciador_notas()