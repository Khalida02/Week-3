arr = input().split()
for n in arr:
    if int(n) % 2 != 0:
        print(min(n))