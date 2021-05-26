students = int(input())
a, b, c, d, av = 0, 0, 0, 0, 0
for i in range(students):
    grade = float(input())
    av += grade
    if grade >= 5: a += 1
    elif grade >= 4: b += 1
    elif grade >= 3: c += 1
    else: d += 1
av = av / students
print(f"Top students: {((a / students) * 100):.2f}%")
print(f"Between 4.00 and 4.99: {((b / students) * 100):.2f}%")
print(f"Between 3.00 and 3.99: {((c / students) * 100):.2f}%")
print(f"Fail: {((d / students) * 100):.2f}%")
print(f"Average: {av:.2f}")
