class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

    def states(self):
        print("India has 28 states")

class USA():
    def capital(self):
        print("Washington D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developing country.")

oi = India()
ou = USA()

for country in (oi, ou):
    country.capital()
    country.language()
    country.type()
    country.states()