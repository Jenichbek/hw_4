class Transport:
    def __init__(self, name, speed):
        self.name= name
        self.speed = speed
    def move(self):
        return f"транспорт {self.name} двигается со скоростью {self.speed}"

class Car(Transport):
    def __init__(self, name, speed, petrol: int):
        super().__init__(name, speed)
        self.petrol = petrol
    def refuel(self, refuel):
        print(f'вы запрвились {self.petrol} + {refuel}')
        self.petrol + refuel
        print(f"{self.petrol}")

        
    def the_road(self):
        print(f"{self.name} едет по дороге")
    

class bike(Transport):
    def bike_road(self):
        print(f"{self.name} едет по велодорожке")

class plane(Transport):
    def sky(self):
        print(f"{self.name} летит по небу")

m = Car(name="Mercedes", speed=50, petrol=10)