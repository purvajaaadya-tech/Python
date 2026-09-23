class ioss():

    def __init__(self):
        self.s1 = ""

    def gs(self):
        self.s1 = input("enter string: ")

    def ps(self):
        print("result is: ", self.s1.upper())

s1 = ioss()

s1.gs()
s1.ps()