class v:
    def __init__(self, b):
        self.b = b

    def st(self):
        print("this is a vehicle")

class c(v):
    def __init__(self, b, m):
        super().__init__(b)
        self.m = m
    
    def st(self):
        print("this is a car")

c1 = c("Audi", "Q3")

print("brand: ", c1.b)
print("model: ", c1.m)

c1.st()

print("is car a subclass of vehicle?", issubclass(c, v))

class b(v):
    def __init__(self, b, m):
        super().__init__(b)
        self.m = m

    def st(self):
        print("this is a bike")

b1 = b("Honda", "Activa")

print("brand: ", b1.b)
print("model: ", b1.m)

b1.st()

print("is bike a subclass of vehicle?", issubclass(b, v))