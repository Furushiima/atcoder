li = []
n = int(input())
li = list(map(int, input().split()))
ans = 0

for i in range(len(li)):
    if li[i] >= 10:
        ans = ans + li[i] - 10

print(ans)