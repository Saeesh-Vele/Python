List1 = []
List2 = []
M  = int(input("Enter the number of Elements in List1 : "))
N  = int(input("Enter the number of Elements in List2 : "))
for i in range(M):
    ele = int(input("Enter the element in List1 : "))
    List1.append(ele)
for i in range(N):
    ele = int(input("Enter the element in List2 : "))
    List2.append(ele)
for i in List2:
    List1.append(i)
List1.sort()
print(List1)