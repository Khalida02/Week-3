n = int(input())
s = dict(input())
for i in range(n):
    first, second = input().split()
    s[first] = second
    s[second] = first
    print(s[input()])