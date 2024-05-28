
def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)
    return sum

add(2, 4, 5, 6, 7, 0)


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add = 3, multiply = 5)

class Car:
    def __init__(self,**kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')


my_car = Car(model="GT-R")
print(my_car.make)