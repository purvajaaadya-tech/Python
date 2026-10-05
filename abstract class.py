from abc import ABC, abstractmethod

class absclass(ABC):
    def print(self,x):
        print("passed value: ", x)

    @abstractmethod
    def task(self):
        print("we are inside absclass task")

class tc(absclass):
    def task(self):
        print("we are inside test_class task")

to = tc()
to.task()
to.print(100)

po = absclass()
po.print()
po.print(200)