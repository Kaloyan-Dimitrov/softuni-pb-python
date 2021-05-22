size = input()
color = input()
count = int(input())
if size == "Large":
    price = 16 if color == "Red" else 12 if color == "Green" else 9
if size == "Medium":
    price = 13 if color == "Red" else 9 if color == "Green" else 7
if size == "Small":
    price = 9 if color == "Red" else 8 if color == "Green" else 5
print(f"{(price * count) * 0.65:.2f} leva.")