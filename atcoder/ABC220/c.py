n = int(input())
a = list(map(int, input().split()))
x = int(input())

a_sum = 0
for i in range(n):
    a_sum += a[i]

m = x // a_sum
ans = m * n
y = m * a_sum

x = x - y
y = 0
i = 0
while(1):
    ans += 1
    y += a[i]
    i += 1
    if(x < y):
        break

print(ans)
