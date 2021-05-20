n = int(input())
current = 1
for i in range(1, n + 1):
    for j in range(i, i + i):
        print(current, end=' ')
        current += 1
        if(current > n): 
            break
    print()
    if(current > n):
        break
