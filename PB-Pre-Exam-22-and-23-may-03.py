dancers = int(input())
points = float(input())
season = input()
place = input()
sum = dancers * points if place == "Bulgaria" else dancers * points * 1.5
if place == "Bulgaria": 
    sum = sum * 0.95 if season == "summer" else sum * 0.92
else:
    sum = sum * 0.90 if season == "summer" else sum * 0.85
left = 0.25 * sum
print(f"Charity - {(sum * 0.75):.2f}")
print(f"Money per dancer - {(left / dancers):.2f}")
