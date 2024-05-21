class Animal:
    def __init__(self):
        self.num_eyes = 2

    def heartbeat(self):
        print('thump thump')

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving through water!")

    def heartbeat(self):
        super().heartbeat()
        print("heart beating and water moving through gills!")

nemo = Fish()
nemo.heartbeat()
nemo.swim()

