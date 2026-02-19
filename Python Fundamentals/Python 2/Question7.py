print("Enter number to check Positive and Negative or0 to exit")
n = int(input("Enter the number :"))

while n != 0:
    if n < 0:
        print("Negative")
    elif n > 0:
        print("Positive")
    elif n == 0:
        print("Its a Zero and you Quited the Program")
        break
    n = int(input("Enter the number :"))