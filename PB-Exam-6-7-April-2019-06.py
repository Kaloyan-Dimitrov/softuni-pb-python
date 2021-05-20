name = input()
student = 0
standard = 0
kid = 0
grand_total = 0
while name != 'Finish':
    places = int(input())
    taken = 0
    for i in range(places):
        type = input()
        if type == 'End': 
            break
        else: 
            taken += 1
            if type == 'student':
                student += 1
            elif type == 'kid': 
                kid += 1
            elif type == 'standard':
                standard += 1
    percentage = (taken / places) * 100
    grand_total += taken
    print(f"{name} - {percentage:.2f}% full.")
    name = input()
print(f'Total tickets: {grand_total}')
student = student / grand_total * 100
print(f'{student:.2f}% student tickets.')
standard = standard / grand_total * 100
print(f'{standard:.2f}% standard tickets.')
kids = kid / grand_total * 100
print(f'{kids:.2f}% kids tickets.')
