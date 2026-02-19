def calculator(a , b ,operation):
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b 
        case "/":
            return a / b 
        case _ :
            return "Invalid Operation"

a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
operation = input("Enter the operation (+, -, *, /): ")

result = calculator(a, b, operation)
print("Result:", result)