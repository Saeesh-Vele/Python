List1 = [1 , 2 , 3 , 4 , 5 , 5 , 5 , 4 ]
L1 = set()
L2 = set()
for val in List1:
    if val not in L1 :
        L1.add(val)
    else:
        L2.add(val)
print(L2)