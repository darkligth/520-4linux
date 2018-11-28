#!/usr/bin/python3

class Conta ():
    '''Tentando abstrair uma conta corrente '''
    def __init__(self, n_conta, saldo):
        self.conta = n_conta
        self.saldo = saldo

    def sacar (self, valor:int) -> bool:
        ''' funcao para sacar um valor da conta '''
        if self.saldo > valor:
            self.saldo -= valor
            return True
        else:
            return False

    def depositar(self, valor):
        ''' funcao para sacar um valor da conta'''
        self.saldo += valor
        return self.saldo

    def transferir(self, valor, conta):
        '''funcao para transferir um valor da conta'''
        try:
           if not self.sacar (valor):
               raise ValueError ("Falha na transferencia")
           try:
                conta.depositar(valor)    
           except AttributeError:
                print("Objeto destino nao possui o metodo depositar!")   
                self.depositar(valor)
        except Exception as e:
            print('Erro: {}'.format(e))

        


c1 = Conta(12345, 1000)
c2 = Conta(6666, 1500)

c1.transferir(500, c2)
print(c1.saldo, c2.saldo)
