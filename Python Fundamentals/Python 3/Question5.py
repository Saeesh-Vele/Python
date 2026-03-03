dict = {"Raj" : 25 , "Amit" : 30 , "Vijay" : 28 , "Rahul" : 32}
print("\nMENU")
print("A - Add a student")
print("B - Update marks")
print("C - Search for a student")
print("D - Display all students")
opp = input("Enter the Opperation : ")
match opp:
    case "A":
        student = input("Enter the new student to add : ")
        marks = int(input("Enter the marks of the Student added : "))
        dict.update({student : marks})
    case "B":
       student = input("Enter the student to update : ")
       up_marks = int(input("Enter the marks to update : "))    
       dict.update({student : up_marks})
    case "C":
        student = input("Enter the student to search : ")
        result = dict.get(student)
        if result is not None:
            print("Marks of "+ student + " is " + str(result))
        else:
            print("Student not found.")
    case "D":
        print(dict)
    case _:
        print("Invalid operation.")