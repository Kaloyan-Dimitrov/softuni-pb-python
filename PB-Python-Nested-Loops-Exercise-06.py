n = int(input())
for i in range(1111, 10000): 
    special = True
    i_copy = i
    while i != 0 and special:
        d = i % 10
        if d == 0:
            special = False
        elif n % d != 0: 
            special = False
        i //= 10
    if special: print(i_copy, end=' ')
        
