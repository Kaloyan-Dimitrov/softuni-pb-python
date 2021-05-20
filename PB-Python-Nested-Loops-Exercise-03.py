num = input()
prime_sum = 0
non_prime_sum = 0
while num != 'stop':
    num = int(num)
    if num < 0:
        print("Number is negative.")
        num = input()
        continue
    prime = True
    if num < 2:
        prime = False
    if prime: 
        for i in range(2, num // 2 + 1):
            if num % i == 0: 
                prime = False
                break
    if prime: 
        prime_sum += num
    else: 
        non_prime_sum += num
    num = input()

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')
