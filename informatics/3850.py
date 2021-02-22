arr = input().split()
for i in arr:
    if i == '0':
        arr.pop(i)
    arr.append(i)
    print(arr)