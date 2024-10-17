# 6 - VERIFICANDO PALÍNDROMOS
# Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strongs para invertes a palavra e comparar com a original.

palavra = input("Digite uma palavra: ").lower()

palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo!")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.!")