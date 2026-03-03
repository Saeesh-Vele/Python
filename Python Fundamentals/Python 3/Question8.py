List1 = [1, 2, 3, 4, 5]
List2 = [6, 4 , 8, 9, 10]
L1 = set()
L2 = set()
for i in List1:
    L1.add(i)
for i in List2:
    L23.add(i)
intersection = L1.intersection(L2)
if len(intersection) == 0:
    print("No common elements found.")
else:
    print("Common elements found: ", intersection)