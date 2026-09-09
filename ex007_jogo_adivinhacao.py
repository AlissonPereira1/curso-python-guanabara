from random import randint
computador = randint(0, 10)
print("Olá! Sou o computador e pensei em um número entre 0 e 10.")
print("Tente adivinhar qual foi!")
acertou = False
total_palpites = 0
while not acertou:
    jogador = int(input("Qual é o seu palpite? "))
    total_palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("É um número maior... Tente novamente.")
        elif jogador > computador:
            print("É um número menor... Tente novamente.")
print(f"Parabéns! Você acertou com {total_palpites} tentativas.")