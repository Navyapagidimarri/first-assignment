from abc import *
class vehicle(ABC):
    def __init__(self,n):
        self.n=n
    @abstractmethod
    def start(self):
        pass

class bike(vehicle):
    def __init__(self,n):
        self.n=n
    def start(self):
        print("i have 2 tyres")

class car(vehicle):
    def __init__(self,n):
        self.n=n
    def start(self):
        print("i have 4 tyres")
class auto(vehicle):
    def __init__(self,n):
        self.n=n
    def start(self):
        print("i have 3 tyres")
b=bike(2)
c=car(4)
a=auto(3)
b.start()
c.start()
a.start()