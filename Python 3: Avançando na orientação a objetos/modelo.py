class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def dar_like(self):
        self._likes += 1


# Herdando da classe Programa
class Filme(Programa):
    # Utilizando o construtor da classe Pai
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme("Vingadores - Guerra infinita", 2018, 160)
print(vingadores.nome)
vingadores.dar_like()

atlanta = Serie("Atlanta", 2018, 2)
