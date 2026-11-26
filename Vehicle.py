class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
ob=Vehicle(200,30)
print("The maximum speed of the car is:",ob.max_speed)
print("The mileage of the car is:",ob.mileage)