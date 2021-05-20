n = int(input())
name = input()
sum_all = 0
count_all = 0
while name != 'Finish':
    sum = 0
    for i in range(0, n):
        sum += float(input())
    average = sum / n
    sum_all += sum
    count_all += n
    print(f'{name} - {average:.2f}.')
    name = input()
print(f'Student\'s final assessment is {sum_all / count_all:.2f}.')
