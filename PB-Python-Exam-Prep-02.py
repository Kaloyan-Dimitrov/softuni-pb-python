minutes = int(input())
seconds = int(input())
length = float(input())
pace = int(input())
control = minutes * 60 + seconds
extra_time = (length / 120) * 2.5
time = (length / 100) * pace - extra_time
if(time > control): print(f"No, Marin failed! He was {(time - control):.3f} second slower.")
else: 
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {time:.3f}.")