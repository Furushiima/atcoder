n, k = map(int, input().split())

ans = 0
for a in range(n):
    for b in range(k):
        ans = ans + (a+1)*100 + (b+1)

print(ans)
