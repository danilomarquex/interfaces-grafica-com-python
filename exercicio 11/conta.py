class Conta(object):
    def __init__(self, id_conta, id_cliente, saldo, limite):
        self.id_conta = id_conta
        self.id_cliente = id_cliente
        self.saldo = saldo
        self.limite = limite
        self.debito = 0
    
    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo = self.saldo - valor
            if self.saldo < 0:
                self.debito=-(self.saldo)
                self.limite=self.limite+self.saldo
                self.saldo=0
            return True 
        else:
            return False
    
    def transferir(self, valor, c):
        if self.sacar(valor):
            c.depositar(valor)
            return True
        else:
            return False
    
    def depositar(self,valor):
        if self.debito > 0:
            if (valor <= self.debito):
                self.debito -= valor
                self.limite += valor
            else:
                dif = valor - self.debito
                self.saldo += dif
                self.limite += self.debito
                self.debito = 0
        else:
            self.saldo += valor

    def mostraSaldo(self):
        return ' Saldo: %.2f Limite: %.2f' %(self.saldo,self.limite)

