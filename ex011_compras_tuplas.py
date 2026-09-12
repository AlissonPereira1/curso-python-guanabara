catalago = ('Café', 18.50, 10, 'Arroz', 22.00, 5, 'Feijão', 11.25, 6,
            'Açucar', 8.99, 5, 'Sal', 3.99, 4, 'Macarrão', 5.45, 7,
            'Óleo', 9.45, 6, 'Vinagre', 4.50, 3, 'Azeite', 5.55, 6)

print('-'*30)
print(f"{'Carrinho de Compras':^30}")
print('-'*30)

valor_total = menor_estoque = mais_caro = 0
produto_mais_caro = produto_menos_estoque = ''

for pos in range(0, len(catalago),3):
    produto = catalago[pos]
    preco = catalago[pos+1]
    quantidade = catalago[pos+2]

    print(f'{produto:<10} R$ {preco:<6.2f} Uni: {quantidade:>1}')

    valor_total += (quantidade * preco)

    if pos == 0 or preco > mais_caro:
        mais_caro = preco
        produto_mais_caro = produto

    if pos == 0 or quantidade < menor_estoque:
        menor_estoque = quantidade
        produto_menos_estoque = produto

print('-' * 30)
print(f'Valor total da compra: R$ {valor_total:.2f}')
print(f'O produto mais caro foi o {produto_mais_caro}, que custa R$ {mais_caro:.2f}.')
print(f'O produto com menor estoque é o {produto_menos_estoque}, com apenas {menor_estoque} unidades.')