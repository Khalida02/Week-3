arr = input().split()
cnt = 1
for i in range(0, len(arr)-1):
    if arr[i] != arr[i+1]:
        cnt += 1

print(cnt)