principal = input("Enter the principal amount :")
rate = input("Enter the rate of intrest : ")
time = input("Enter the times in years : ")
principal = float(principal)
rate = float(rate)
time = float(time)
SI = (principal * rate * time) /100
print("Simple Interest is : " + str(SI))