n = int(input("Enter the Number :"))
X = 0
while (n != 0):
    A = n % 10
    X += A
    n = n // 10
print("The sum of the digits is " + str(X))