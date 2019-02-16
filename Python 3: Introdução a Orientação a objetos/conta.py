# declarando uma classe Conta
class Conta:
    # criando construtor, o self é a referencia da classe
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"saldo {self.__saldo} do titular {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo (self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, valor):
        self.__limite = valor

conta = Conta(10, 'paulo', 150, 500)
conta2 = Conta(11, 'teste', 200, 500)
conta2.transferir(20, conta)
conta2.extrato()
conta.extrato()
conta.deposita(50)
conta.extrato()
conta.saca(10)
conta.extrato()