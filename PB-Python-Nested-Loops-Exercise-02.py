a = int(input())
b = int(input())
for i in range(a, b + 1):
    sumo, sume = (0, 0)
    for index, digit in enumerate(str(i)):
        if index % 2 == 0:
            sume += int(digit)
        else:
            sumo += int(digit)
    if sumo == sume: print(i, end=" ")
