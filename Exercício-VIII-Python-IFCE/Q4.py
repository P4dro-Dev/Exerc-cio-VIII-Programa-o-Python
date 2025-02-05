# 4. Crie um programa onde dois jogadores possam competir no clássico jogo "Pedra, Papel ou Tesoura".
# O programa deve:
# 1. Solicitar que cada jogador informe sua escolha (entre "Pedra", "Papel" ou "Tesoura").
# 2. Determinar o resultado da rodada, exibindo uma das seguintes mensagens:
#    i. "Pedra venceu!"
#    ii. "Tesoura venceu!"
#    iii. “Papel venceu!”
#    iv. "Empate!" (se ambos escolherem a mesma opção).
# As regras para decidir o vencedor são:
# • Pedra ganha de Tesoura (Pedra quebra Tesoura).
# • Tesoura ganha de Papel (Tesoura corta Papel).
# • Papel ganha de Pedra (Papel embrulha Pedra).
# Exemplo de entrada Exemplo de saída
# Pedra
# Tesoura
# Pedra venceu!
# Tesoura Tesoura venceu!
# Papel
# Papel
# Pedra
# Papel venceu!
# Pedra
# Pedra
# Empate

def jogar_pedra_papel_tesoura():
    """
    Simula uma rodada do jogo Pedra, Papel ou Tesoura entre dois jogadores.
    """

    jogador1 = input("Jogador 1, escolha Pedra, Papel ou Tesoura: ").lower()
    jogador2 = input("Jogador 2, escolha Pedra, Papel ou Tesoura: ").lower()

    if jogador1 not in ["pedra", "papel", "tesoura"] or jogador2 not in ["pedra", "papel", "tesoura"]:
        print("Escolhas inválidas. Certifique-se de digitar Pedra, Papel ou Tesoura.")
        return

    match jogador1, jogador2:
        case "pedra", "tesoura":
            print("Pedra venceu!")
        case "tesoura", "papel":
            print("Tesoura venceu!")
        case "papel", "pedra":
            print("Papel venceu!")
        case jogador1, jogador2 if jogador1 == jogador2:
            print("Empate!")
        case _:
            print(f"{jogador2.capitalize()} venceu!")

jogar_pedra_papel_tesoura()