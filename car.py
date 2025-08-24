class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Default Attribute Value
        
    def get_descriptive_name(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name
    
    def get_odometer_reading(self):
        print(f"This car has {self.odometer_reading} miles on it")
        
    def update_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("you cant roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading + miles                