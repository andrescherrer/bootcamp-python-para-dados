# Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

print("Data dd/mm/aaaa e exiba separado")

data = input("Entre com uma data no formato dd/mm/aaaa")

dia, mes, ano = data.split('/')

print("Dia: ", dia)
print("Mês: ", mes)
print("Anp: ", ano)