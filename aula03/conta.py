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

    def __str__(self):
        return 'Conta: {} Saldo: {}'.format(self.conta, self.saldo)

class Poupanca (Conta):
    def __init__(self, n_conta, saldo=0):
        super().__init__(n_conta, saldo)
        self.taxa_juros = 0.005

    def reder_juros(self, n_conta, saldo=0):        
        self.saldo += self.saldo * self.taxa_juros