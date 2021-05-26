fats = float(input())
protein = float(input())
carbs = float(input())
calories = float(input())
waters = float(input())
fats = (fats * calories) / 9
protein = (protein * calories) / 4
carbs = (carbs * calories) / 4
grams = fats + protein + carbs
cl = (calories / grams) * (100 - waters)
print(f"{cl:.4f}")
