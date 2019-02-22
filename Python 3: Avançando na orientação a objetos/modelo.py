from abc import ABCMeta, abstractmethod

class Programa(metaclass= ABCMeta):
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

    # Tornando metodo obrigatóriamente subscrito pelas classes filhas
    @abstractmethod
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


class Playlist:
    def __init__(self, nome, programas):
        self._programas = programas
        self.nome = nome

    # Duck Typing, tornando a classe iteravel
    def __getitem__(self, item):
        return self._programas[item]

    # A classe vai implementar o uso do metodo built-in len()
    def __len__(self):
        return len(self._programas)


vingadores = Filme('Vingadores - Guerra infinita', 2018, 160)
vingadores.dar_like()
tmep = Filme('Todo mundo em panico', 1999, 100)
atlanta = Serie('Atlanta', 2018, 2)
demolidor = Serie('Demolidor', 2016, 2)
vingadores.dar_like()
tmep.dar_like()
atlanta.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(repr(programa))
