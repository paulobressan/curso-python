class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def dar_like(self):
        self.__likes += 1


class Serie:
    def __init__(self, nome, ano, temporada):
        self.__nome = nome.title()
        self.ano = ano
        self.temporada = temporada
        self.__likes = 0

    def dar_like(self):
        self.likes += 1


vingadores = Filme("Vingadores - Guerra infinita", 2018, 160)
print(vingadores.nome)
vingadores.dar_like()

atlanta = Serie("Atlanta", 2018, 2)
