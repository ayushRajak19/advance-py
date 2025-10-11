class Car:

    def __init__(self,brand,color,speed):
        self.b = brand
        self.c = color
        self.s  = speed
        
    def start(self):
        print(f"{self.b} has started")

    def stop(self):
        print(f"{self.b} has stopped")

    

car1 = Car("BMW","RED","250kmph")
car2 = Car("Mercedize","Black","300kmph")
car3 = Car("Porche","White","400kmph")

car1.start()