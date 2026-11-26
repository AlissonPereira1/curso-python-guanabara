"""
personagem.py

Módulo responsável por definir a estrutura e o comportamento dos personagens.

Contém a classe abstrata Personagem e suas classes filhas Guerreiro e Mago.

Centraliza as regras de ataque, recebimento de dano, cura e controle de vida.
"""

# ABC permite criar classes abstratas.
# abstractmethod define métodos que devem ser implementados pelas classes filhas.
from abc import ABC, abstractmethod

# randint realiza sorteios de números inteiros.
# choice seleciona aleatoriamente um elemento de uma coleção.
from random import randint, choice

# Importa o print estilizado da biblioteca Rich.
from rich import print


# Classe abstrata que define a estrutura e os comportamentos comuns dos personagens.
class Personagem(ABC):

    # Atributo de classe: lista fixa de golpes compartilhada pelos personagens.
    GOLPES: tuple[str, ...] = (
        "Soco",
        "Chute",
        "Voadora",
        "Cabeçada"
    )

    # Construtor: inicializa os atributos de cada personagem.
    def __init__(self, nome: str, vida: int, forca: int) -> None:

        # Remove espaços desnecessários do início e do final do nome.
        nome = nome.strip()

        # Valida os dados antes de criar o personagem.
        if not nome:
            raise ValueError("Nome inválido!")

        if vida <= 0:
            raise ValueError("A vida tem que ser maior que zero!")

        if forca <= 0:
            raise ValueError("A força tem que ser maior que zero!")

        # Atributos de instância: cada personagem possui seus próprios valores.
        self.nome = nome
        self.vida = vida
        self.forca_max = forca
        self.saldo_cura = 0
        self.esta_vivo = True

    # Realiza um ataque contra outro personagem.
    # O parâmetro alvo recebe o objeto que será atacado.
    def atacar(self, alvo: "Personagem") -> None:

        # Permite atacar somente quando os dois personagens estão vivos.
        if self.esta_vivo and alvo.esta_vivo:

            # Sorteia o dano respeitando a força máxima do atacante.
            dano = randint(1, self.forca_max)

            # Escolhe aleatoriamente um golpe da coleção GOLPES.
            golpe = choice(self.GOLPES)

            # Exibe as informações do ataque no terminal.
            print(
                f"[blue]{self.nome}[/]([magenta]{self.vida}[/]) "
                f"atacou [red]{alvo.nome}[/]([magenta]{alvo.vida}[/]) "
                f"com um/uma [yellow]{golpe}[/] de força [magenta]{self.forca_max}[/]"
            )

            # Chama o método receber_dano() do personagem atacado.
            alvo.receber_dano(dano)

        else:

            # Verifica se os dois personagens estão derrotados.
            if not self.esta_vivo and not alvo.esta_vivo:
                print(f"[red]{self.nome}[/] e [red]{alvo.nome}[/] já estão mortos!")

            # Verifica se somente o atacante está derrotado.
            elif not self.esta_vivo:
                print(f"[red]{self.nome}[/] já foi [red]derrotado[/]! Ele(a) não pode atacar")

            # Se chegou aqui, o alvo está derrotado.
            else:
                print(f"[red]{alvo.nome}[/] já foi [red]derrotado[/]! Ele(a) não pode receber mais danos")

    # Processa o dano recebido pelo personagem.
    def receber_dano(self, dano: int) -> None:

        # Impede que um personagem derrotado receba novos danos.
        if self.esta_vivo:

            # Acumula o dano recebido no saldo disponível para cura.
            self.saldo_cura += dano

            # Desconta o dano da vida atual.
            self.vida -= dano

            # Verifica se a vida chegou a zero ou ficou negativa.
            if self.vida <= 0:

                # Impede que a vida fique com um valor negativo.
                self.vida = 0

                # Atualiza o estado do personagem para derrotado.
                self.esta_vivo = False

                print(f"[red]{self.nome}[/] foi derrotado!")

            else:
                # Informa a quantidade de dano recebida.
                print(f"[red]{self.nome}[/] recebeu [red]dano de {dano}[/]!\n")

        else:
            # Informa que o personagem já está derrotado.
            print(f"[red]{self.nome}[/] já foi [red]derrotado[/]! Ele(a) não pode receber mais danos")

    # Realiza a cura do personagem utilizando o saldo acumulado.
    def curar(self) -> None:

        # Impede que personagens derrotados utilizem a cura.
        if self.esta_vivo:

            # Verifica se existe saldo disponível para recuperação de vida.
            if self.saldo_cura > 0:

                # Sorteia a quantidade de vida que será recuperada.
                # O limite máximo é o saldo de cura disponível.
                cura = randint(1, self.saldo_cura)

                # Desconta do saldo a quantidade utilizada na cura.
                self.saldo_cura -= cura

                # Adiciona a quantidade recuperada à vida atual.
                self.vida += cura

                # Exibe a mensagem personalizada de cura do personagem.
                print(
                    f"[red]{self.nome}[/] {self.texto_cura} e "
                    f"[green]recuperou {cura} pontos[/] de vida\n"
                )

            else:
                # Informa que não existe saldo disponível para recuperação.
                print("Saldo de cura indisponível!")

        else:
            # Impede que personagens derrotados realizem a cura.
            print(f"[red]{self.nome}[/] já foi derrotado! Ele não pode se curar")

    # Propriedade abstrata que exige uma descrição de cura nas classes filhas.
    @property
    @abstractmethod
    def texto_cura(self) -> str:
        pass


# Classe filha que herda os atributos e comportamentos de Personagem.
class Guerreiro(Personagem):

    # Implementa a propriedade abstrata com uma descrição específica do Guerreiro.
    @property
    def texto_cura(self) -> str:
        return "enrolou uma atadura nos ferimentos"


# Classe filha que herda os atributos e comportamentos de Personagem.
class Mago(Personagem):

    # Implementa a propriedade abstrata com uma descrição específica do Mago.
    @property
    def texto_cura(self) -> str:
        return "conjurou uma magia de cura"

