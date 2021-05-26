night = input()
base = 5364
day = 1
while night != "END":
    meters = int(input())
    if night == "Yes": day += 1
    base += meters
    if base >= 8848: break
    if day == 6: 
        base -= meters
        break
    night = input()
if base >= 8848:
    print(f"Goal reached for {day} days!")
else: 
    print("Failed!")
    print(base)