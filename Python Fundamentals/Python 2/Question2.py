
def AllEvenInBtw(a,b):
    for i in range (a , b+1):
        if (i%2 ==0):
            print(i)
a = int(input("Enter the start number :"))
b = int(input("Enter the end number :"))
AllEvenInBtw(a,b)