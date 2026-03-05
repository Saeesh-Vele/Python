class Products:     
    store_name = "RK Medicines"
    total_count = 0
    
    def __init__ (self,name,price):         
        self.name = name         
        self.price = price 
        Products.total_count += 1
    
    def get_info(self):
        print(f"The Medicine name is {self.name} and price is {self.price}")
    
    @classmethod
    def get_totel_count(cls):
        print(f"The total count of Medicins is {cls.total_count}")
    
    @staticmethod 
    def cal_discount(price,discount):         
        final_price = price - (discount*price/100)         
        print(f"Discounted Price is {final_price}")
          
Med1 = Products("Kurex" , 1200)
Med1.get_info()
Med1.cal_discount(1200 , 10)
Med1.get_totel_count()