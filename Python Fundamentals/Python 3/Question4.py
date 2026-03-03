tup = (1 , 2, 3, 4, 5, 6)
even_tup = ()
odd_tup = ()
for i  in tup :
    if i%2 == 0 :
        even_tup += (i,)
    else:
        odd_tup += (i,)
print("Even Tuple : ", even_tup)
print("Odd Tuple : ", odd_tup)
