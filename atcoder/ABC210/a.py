n, a, x, y = map(int, input().split())

ans = n*x
if(n > a):
    ans -= ((n - a) * (x - y))

print(ans)
