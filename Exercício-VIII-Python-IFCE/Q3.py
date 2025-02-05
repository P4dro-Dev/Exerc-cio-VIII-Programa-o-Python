# Faça um programa que solicite do usuário o consumo de energia elétrica em kWh e calcule o valor da
# conta com base no consumo:
# • Até 100 kWh: R$ 0,50 por kWh.
# • De 101 a 300 kWh: R$ 0,75 por kWh.
# • Acima de 300 kWh: R$ 1,00 por kWh.
# Adicione ainda uma taxa fixa de R$ 5,00 para todos os casos.
#
# Exemplo de entrada Exemplo de saída
# 50 Total = R$ 30.00
# 200 Total = R$ 155.00
# 400 Total = R$ 405.00


consumo = float(input("Digite o consumo de energia em kWh: "))

if consumo <= 100:
    valor = consumo * 0.50
elif 101 <= consumo <= 300:
    valor = consumo * 0.75
else:
    valor = consumo * 1.00

# Adiciona a taxa fixa de R$ 5,00
valor_total = valor + 5.00

# Exibe o valor total da conta
print(f"Total = R$ {valor_total:.2f}")