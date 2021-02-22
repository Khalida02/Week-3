arr = input().split()

for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        print(arr[i])