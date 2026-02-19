n = int(input("Enter the Number :"))
count = 0
while (n != 0):
    A = n % 10
    count += 1
    n = n // 10
print("The number of digits in the given number is " + str(count))