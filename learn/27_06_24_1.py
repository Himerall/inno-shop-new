class Car:
    def __init__(self,color):
        self.color = color

    def __add__(self,other):
        return Number(self.n + other.n)
    
    def __str__(self):
        return f'Number: {self.n}'
car = Car('red')

print(car)