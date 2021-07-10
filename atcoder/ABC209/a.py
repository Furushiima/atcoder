a, b = map(int, input().split())

if a > b :
    ans = 0
else:
    ans = b - a + 1

print(ans)
