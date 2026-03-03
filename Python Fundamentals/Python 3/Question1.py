str = input("Enter a string: ")
rev_str = ""
for ch in str:
    rev_str = ch + rev_str
if str == rev_str:
    print("Palindrome")
else:
    print("Not a palindrome")