from numpy.distutils.system_info import atlas_3_10_blas_info


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

    # Metodo subscrito para sobrescrever o texto de retorno padrão da classe
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'


# Herdando da classe Programa
class Filme(Programa):
    # Utilizando o construtor da classe Pai
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes - {self.duracao} duração'

    def __repr__(self):
        return f"Filme(nome = '{self._nome}', ano = {self.ano}, duração = {self.duracao}, likes = {self.likes})"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes {self.temporadas} temporadas'


vingadores = Filme("Vingadores - Guerra infinita", 2018, 160)
vingadores.dar_like()

atlanta = Serie("Atlanta", 2018, 2)

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    print(repr(programa))
