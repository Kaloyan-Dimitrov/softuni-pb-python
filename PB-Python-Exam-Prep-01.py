name = input()
seasons = int(input())
episodes = int(input())
length = float(input())
ads = length * 0.2
real_length = length + ads
special_episodes = seasons * 10
time = real_length * episodes * seasons + special_episodes
print(f"Total time needed to watch the {name} series is {time:.0f} minutes.")