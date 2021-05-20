n = int(input())
l = int(input())
for f in range(1, n):
    for s in range(1, n):
        for t in range(ord('a'), ord('a') + l):
            for fo in range(ord('a'), ord('a') + l):
                for fi in range(f + 1 if f > s else s + 1, n + 1):
                    print(str(f) + str(s) + chr(t) + chr(fo) + str(fi), end=' ')
