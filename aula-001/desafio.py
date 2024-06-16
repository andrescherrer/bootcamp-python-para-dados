BONUS_2024 = 1000
nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o valor do salário: "))
bonus_percentual = float(input("Digite o % do bônus: "))
valor_bonus = BONUS_2024 + salario * bonus_percentual

print(f"O funcionário {nome} vai receber {valor_bonus}")

