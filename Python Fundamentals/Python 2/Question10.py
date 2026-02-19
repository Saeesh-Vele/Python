n = int(input("Guess the number :"))
x = 7
while n != x:
    if n < x:
        print("Too low")
    elif n > x:
        print("Too high")
    n = int(input("Guess the number again :"))
print("Congratulations! You guessed the number.")