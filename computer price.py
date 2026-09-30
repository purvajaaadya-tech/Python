class com:
    def __init__(self):
        self.__mp = 900

    def sell(self):
        print("selling price: {}".format(self.__mp))

    def smp(self, p):
        self.__mp = p

c = com()
c.sell()

c.__mp = 1000
c.sell()

c.smp(1000)
c.sell()