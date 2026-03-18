# Define uma lista de números
numeros = [3, 7, 2, 9, 5]

# Pega o primeiro número pelo index
maior = numeros[0]

# Percorre a lista de números
for n in numeros:
    if n > maior:             # Checa se o número percorrido é maior que o atual maior
        maior = n             # Se for, vira o novo maior número

# Exibe o maior número encontrado
print(maior)
