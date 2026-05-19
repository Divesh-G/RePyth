class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("hundai")

print(car1.start())
print(car1.color)