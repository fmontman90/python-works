from tire import Tire

tire = Tire('P', 205, 55, 15)
tires =[tire,tire,tire,tire]
#This example of class
class Car:
    """
    Car models a car with tires and an engine
    """
    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

    def description(self):
        print(f"A car with an {self.engine} engine, and {self.tires} tires")
    
    def wheel_circumference(self):
        if len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return 0

    

#defining the civic model
civic = Car('4-cylinder', ['front-passenger', 'front-passenger', 'rear-driver', 'rear-passenger'] )
#Should print the above info for civic.
civic.description() #If you run print instead you get None at the end.
#print(civic.tires)

#definig the honda model kind of generic I know 
honda = Car(tires=tires, engine='4-cylinder')
honda.description()
print(honda.wheel_circumference())

