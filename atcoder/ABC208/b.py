import math

p = int(input())
ans = 0
k = []
# 10! < 10^7 < 11!
for i in range(11):
    k.append(math.factorial(i+1))

for i in range(11):
    j = 10-i
    while(1):
        if(p >= k[j]):
            p = p - k[j]
            ans += 1
        else:
            break

print(ans)
