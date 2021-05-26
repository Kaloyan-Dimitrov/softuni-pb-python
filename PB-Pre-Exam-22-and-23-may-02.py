price = float(input())
love = int(input())
roses = int(input())
key = int(input())
car = int(input())
lucky = int(input())
sum = love * 0.6 + roses * 7.2 + key * 3.6 + car * 18.2 + lucky * 22
count = love + roses + key + car + lucky
if(count > 25): sum = sum * (1 - 0.35)
sum = sum * 0.9
if(sum > price): print(f"Yes! {sum - price:.2f} lv left.")
else:
    print(f"Not enough money! {price - sum:.2f} lv needed.")
