arr = input().split()

for i in range(0, len(arr) - 1):
    if int(arr[i]) * int(arr[i + 1]) > 0:
        print(arr[i], arr[i + 1])
        break