arr = input().split()
i = input().split()
for i in range(1, len(arr)):
    arr.pop(int(arr[i]))
    print(arr)