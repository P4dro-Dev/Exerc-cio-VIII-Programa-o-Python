# Implemente um programa que receba a temperatura corporal de uma pessoa e exiba uma mensagem
# sobre a situação da saúde, de acordo com a tabela abaixo:
#
# Temperatura Situação
# Menor que 35.0 Hipotermia
# Entre 35.0 e 37.4 Temperatura normal
# Entre 37.5 e 38.0 Estado febril
# Entre 38.1 e 39.9 Febre moderada
# 40.0 ou mais Febre alta - Procure um médico


temperatura = float(input("Digite a temperatura corporal: "))

if temperatura < 35.0:
    print("Hipotermia")
elif 35.0 <= temperatura <= 37.4:
    print("Temperatura normal")
elif 37.5 <= temperatura <= 38.0:
    print("Estado febril")
elif 38.1 <= temperatura <= 39.9:
    print("Febre moderada")
else:
    print("Febre alta - Procure um médico")