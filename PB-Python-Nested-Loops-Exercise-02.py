a = int(input())
b = int(input())
for i in range(a + 1, b):
    sume = 0
    sumo = 0
    for index, c in enumerate(str(i)):
        if index % 2 == 0:
            sume += int(c)
        else: sumo += int(c)
    if sumo == sume: print(i, end=" ")
