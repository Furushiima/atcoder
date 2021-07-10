n, x = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
for i in range(n):
    j = i + 1
    if (j % 2 == 0):
        sum += (a[i] - 1)
    else:
        sum += a[i]

if(sum <= x):
    ans = "Yes"
else:
    ans = "No"

print(ans)
