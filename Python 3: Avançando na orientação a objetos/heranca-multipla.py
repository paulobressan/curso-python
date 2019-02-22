class Funcionario:
    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


class Junior(Alura):
    pass


# Implementando herança multipla
class Pleno(Alura, Caelum):
    pass


junior = Junior()
junior.busca_perguntas_sem_resposta()
junior.mostrar_tarefas()

pleno = Pleno()
pleno.busca_perguntas_sem_resposta()
pleno.busca_cursos_do_mes()
pleno.mostrar_tarefas()
