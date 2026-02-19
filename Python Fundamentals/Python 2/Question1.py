salary = int(input("Enter your salary :"))
if salary <= 30000:
    print("The Tax applicable is 5% " +" the tax amount is " +str(salary * 0.05))
elif 30000 < salary <= 70000:
    print("The Tax applicable is 15% " +" the tax amount is " +str(salary * 0.15))
elif 70000< salary  :
    print("The Tax applicable is 25% " +" the tax amount is " +str(salary * 0.25))