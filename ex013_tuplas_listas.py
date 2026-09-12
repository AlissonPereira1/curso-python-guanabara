from random import randint

# 1. Sorteio e criação da tupla inicial
numeros_lista = []
for c in range(0, 5):
    num_sorteado = randint(-10, 10)
    numeros_lista.append(num_sorteado)
numeros = tuple(numeros_lista)

# 2. Inicialização de contadores e listas temporárias
cont_positivo = cont_negativo = cont_zeros = 0
positivo_lista = []
negativo_lista = []
zeros_lista = []

# 3. Filtragem dos elementos
for num in numeros:
    if num > 0:
        positivo_lista.append(num)
        cont_positivo += 1
    elif num < 0:
        negativo_lista.append(num)
        cont_negativo += 1
    else:
        zeros_lista.append(num)
        cont_zeros += 1

# 4. Comparação de maior quantidade
if cont_positivo > cont_negativo:
    tupla_maior = 'POSITIVOS'
    cont_tuple = cont_positivo
else:
    tupla_maior = 'NEGATIVOS'
    cont_tuple = cont_negativo

# 5. Conversão final para tuplas
positivo = tuple(positivo_lista)
negativo = tuple(negativo_lista)
zero = tuple(zeros_lista)

# 6. Exibição formatada dos resultados
print('-' * 30)
print(f"{'SEPARADOR DE NUMEROS':^30}")
print('-' * 30)

print(f'Tupla gerada: {numeros}\n')
print(f'Tupla de Positivos: {positivo} [Total: {cont_positivo} números]')
print(f'Tupla de Negativos: {negativo} [Total: {cont_negativo} números]')
if cont_zeros > 0:
    print(f'Tupla de Zeros: {zero} [Total: {cont_zeros} números]')

print(f'\nA tupla com a maior quantidade de elementos foi a de {tupla_maior} ({cont_tuple} elementos)')
