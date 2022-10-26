class TV:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def canal_mais(self):
        if self.ligada:
            self.canal += 1

    def canal_menos(self):
        if self.ligada:
            self.canal -= 1


if __name__ == '__main__':
    tv = TV()
    print("Televisão esta Ligada : {}".format(tv.ligada))
    tv.power()
    print("Televisão esta Ligada : {}".format(tv.ligada))
    tv.power()
    print("Televisão esta Ligada : {}".format(tv.ligada))
    tv.canal_mais()
    print("Televisão esta Ligada : {}".format(tv.ligada))
    tv.canal_mais()
    tv.canal_mais()
    print("Televisão esta no canal : {}".format(tv.canal))
    tv.canal_menos()
    print("Televisão esta no canal : {}".format(tv.canal))
