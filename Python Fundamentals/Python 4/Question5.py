class Vehicle:
    def __init__(self , brand , model ):
        self.brand = brand
        self.model = model
    
    def get_details(self):
        print(f"The brand is {self.brand} and the model is {self.model} ")  
        if hasattr(self , "seats"):
            print(f"Seats = {self.seats}")
        if hasattr(self , "engine_cc"):
            print(f"engine_cc = {self.engine_cc}")
        
class Car(Vehicle):
    def __init__ (self, brand, model, seats):
        super().__init__(brand,model)
        self.seats = seats

class Bike(Vehicle):
    def __init__ (self, brand, model, engine_cc):
        super().__init__(brand,model)
        self.engine_cc = engine_cc

   
B1 = Car("xyz" , "xs" , 4 )
B1.get_details()