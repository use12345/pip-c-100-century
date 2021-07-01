class Cars(object):
    def __init__(self,color,model,speed,fueltype):
        self.color=color
        self.model=model
        self.speed=speed
        self.fueltype=fueltype
    def start(self):
        print("Car Started")
    def stop(self):
        print("Car Stoped")    
    def race(self):
        print("accelerating")
    def gear(self):
        print("Gear Changed")   
car1=Cars("red","ABCD","180km/h","petrol")
print(car1.start())
print(car1.color)


             