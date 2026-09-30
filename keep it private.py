class mc:
    
    __pv = 27;

    def __pm(self):
        print("i am inside class myclass")

    def h(self):
        print("private variable value: ", mc.__pv)

foo = mc()
foo.h()
foo.__pm