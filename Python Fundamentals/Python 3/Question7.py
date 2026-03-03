String = input("Enter a string: ")
count = 0
for char in String:
    if char == " ":
        count += 1
print("Number of spaces:", count)