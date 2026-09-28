class fm:
    def __init__(self, ec, hcm):
        self.ec = ec
        self.hcm = hcm

    def st(self):
        print("eye colour: ", self.ec)
        print("height (cm): ", self.hcm)

class kid(fm):
    def __init__(self, n, a, ec, hcm):
        self.n = n
        self.a = a
        super().__init__(ec, hcm)

    def st(self):
        print("name: ", self.n)
        print("age: ", self.a)
        super().st()

    def fh(self, hobby):
        print(self.n, "loves", hobby)

c = kid("Maya", 10, "brown", 140)

c.st()
c.fh("painting")

print("is kid a subclass of familymember?", issubclass(kid, fm))