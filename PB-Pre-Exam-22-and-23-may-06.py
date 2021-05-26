n = int(input())
found = False
ten = n % 10 == 5
three = n % 3 == 0

# for a in range(1, 10):
#     for b in range(9, a - 1, -1):
#         for c in range(1, 10):
#             for d in range(9, c - 1, -1):
#                 sum = a + b + c + d
#                 prod = a * b * c * d
#                 if sum == prod and ten: 
#                     print(f"{a}{b}{c}{d}")
#                     found = True
#                 if prod // sum == 3 and three:
#                     print(f"{d}{c}{b}{a}")
#                     found = True
#                 if found == True: break
#             if found == True:
#                 break
#         if found == True: break
#     if found == True:
#         break
a = 1
while a < 10 and not(found):
    b = 9
    while b >= a and not(found):
        c = 0
        while c < 10 and not(found):
            d = 9
            while d >= c and not(found):
                sum = a + b + c + d
                prod = a * b * c * d
                if sum == prod and ten:
                    print(f"{a}{b}{c}{d}")
                    found = True
                if prod // sum == 3 and three:
                    print(f"{d}{c}{b}{a}")
                    found = True
                d -= 1
            c += 1
        b -= 1
    a += 1

if not(found): print("Nothing found")
