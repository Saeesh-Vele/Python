class Student:
    def __init__ (self , name , roll_no , marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks
    
    def get_name(self):
        return self.__name
    
    def get_roll_no(self):
        return self.__roll_no
        
    def get_marks(self):
        return self.__marks
    
    def set_name(self , new_name):
        if new_name == "":
            print("Name Cannot Be Empty ")
        else:
            self.__name = new_name
    
    def set_roll_no(self , new_roll_no):
        if 1 <= new_roll_no <= 100:
            self.__roll_no = new_roll_no
        else: 
            print("Roll No must be between 1 and 100")
    
    def set_marks(self , new_marks ):
        if new_marks < 0:
            print("Marks cannot be Negative")
        else:
            self.__marks = new_marks
s1 = Student("Ali", 10, 85)

print(s1.get_name())
print(s1.get_roll_no())
print(s1.get_marks())

s1.set_marks(-5)   # Invalid
s1.set_roll_no(120) # Invalid
s1.set_name("")     # Invalid