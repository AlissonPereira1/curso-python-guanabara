clima_sao_paulo = ('Domingo', 35, 'Segunda', 30, 'Terça', 28, 'Quarta', 25,
                   'Quinta', 31, 'Sexta', 29, 'Sábado', 24)

soma_temp = dias_acima = maior_temp = menor_temp = 0
dia_mais_quente = dia_mais_frio = ''

print('\033[1;35m-' * 30)
print(f'{"TEMPERATURA DA SEMANA":^30}')
print('-' * 30)

for pos in range(0, len(clima_sao_paulo), 2):
    dia = clima_sao_paulo[pos]
    temperatura = clima_sao_paulo[pos + 1]

    # Exibe os dados formatados
    print(f'{dia:<10}{temperatura:>5}°')

    # Soma as temperaturas para calcular a média depois
    soma_temp += temperatura

    # Identifica o dia mais quente e o mais frio
    if pos == 0:
        maior_temp = menor_temp = temperatura
        dia_mais_quente = dia_mais_frio = dia
    else:
        if temperatura > maior_temp:
            maior_temp = temperatura
            dia_mais_quente = dia
        if temperatura < menor_temp:
            menor_temp = temperatura
            dia_mais_frio = dia

# Calcula a média real com o total somado após o laço
media_temp = soma_temp / (len(clima_sao_paulo) / 2)

# Conta quantos dias ficaram acima da média já calculada
for pos in range(1, len(clima_sao_paulo), 2):
    if clima_sao_paulo[pos] >= media_temp:
        dias_acima += 1

print('\033[1;35m-\033[m' * 37)
print(f'\033[1;33mMédia da temperatura da semana: {int(media_temp)}°')
print(f'Na semana, {dias_acima} dias ficaram acima da média.')
print(f'O dia mais quente foi {dia_mais_quente}, com {maior_temp}º.')
print(f'O dia mais frio foi {dia_mais_frio}, com {menor_temp}º.\033[m')