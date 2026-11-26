"""
main.py

Arquivo principal do projeto.
Responsável por criar os personagens, controlar o combate,
sortear os ataques e apresentar o resultado da partida.

As classes Guerreiro, Mago e Personagem estão definidas
no módulo personagem.py.
"""


# Importa Sequence para tipar coleções de objetos Personagem
from collections.abc import Sequence

# Importa as classes do arquivo personagem.py
from personagem import Personagem, Guerreiro, Mago

# Importa o print estilizado do Rich
from rich import print

# Importa choice para realizar escolhas aleatórias
from random import choice


# Exibe um título centralizado no terminal
def titulo(msg: str) -> None:
    print(f' {msg} '.center(39, '=') + "\n")


# Recebe uma coleção de personagens e apresenta seus atributos
def personagens_status(personagens: Sequence[Personagem]) -> None:
    titulo("PERSONAGENS")

    # Percorre todos os personagens da coleção
    for personagem in personagens:
        print(f"[blue]{personagem.nome}[/]")
        print(f"[green]Vida:[/] {personagem.vida}")
        print(f"[green]Força:[/] {personagem.forca_max}")

        # Exibe Vivo ou Morto conforme o estado do personagem
        print(f"[green]Status:[/] {'Vivo' if personagem.esta_vivo else 'Morto'}\n")


# Função principal: controla a execução do jogo
def main() -> None:

    # Cria os personagens com seus respectivos atributos
    p1 = Guerreiro("Kratos", 1000, 1000)
    p2 = Mago("Merlin", 1000, 700)

    # Armazena os objetos em uma lista
    personagens = [p1, p2]

    # Exibe os atributos iniciais dos personagens
    personagens_status(personagens)

    titulo("COMBATE")

    # O combate continua enquanto os dois personagens estiverem vivos
    while p1.esta_vivo and p2.esta_vivo:

        # Sorteia aleatoriamente quem começa atacando nesta rodada
        primeiro_atacante = choice(personagens)

        # Define o outro personagem como segundo atacante
        segundo_atacante = p1 if primeiro_atacante == p2 else p2

        # O primeiro personagem realiza o ataque
        primeiro_atacante.atacar(segundo_atacante)

        # O segundo personagem só contra-ataca se continuar vivo
        if segundo_atacante.esta_vivo:
            segundo_atacante.atacar(primeiro_atacante)

        # A cura só acontece se os dois personagens continuarem vivos
        if primeiro_atacante.esta_vivo and segundo_atacante.esta_vivo:
            segundo_atacante.curar()
            primeiro_atacante.curar()

    # Verifica qual personagem venceu após o encerramento do combate
    if p1.esta_vivo and not p2.esta_vivo:
        vencedor = f"[blue]{p1.nome}[/] venceu!"

    elif p2.esta_vivo and not p1.esta_vivo:
        vencedor = f"[blue]{p2.nome}[/] venceu!"

    else:
        # Caso os dois estejam mortos, informa o empate
        vencedor = f"Empate! {p1.nome} e {p2.nome} estão mortos"

    # Exibe o resultado final do combate
    print(vencedor)

    # Mostra os atributos atualizados após a batalha
    personagens_status(personagens)

    # Ferramentas de inspeção para analisar os objetos durante o desenvolvimento
    # Para utilizá-las, importe inspect do Rich:
    # inspect(p1, methods=True)
    # inspect(p2, methods=True)


# Verifica se este arquivo está sendo executado diretamente
# Se estiver, chama a função principal
if __name__ == "__main__":
    main()