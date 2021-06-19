import collections 

n = int(input())
a = list(map(int, input().split()))
ans = 0

# LTE
# m = n-1
# for i in range(n-1):
#     for j in range(m):
#         if a[i] != a[i+j+1]:
#             ans += 1
#     m -= 1

c = collections.Counter(c)
 
for i in range(n-1):
    ans += n-1-i
    ans -= (c[a[i]] - 1)
    if(c[a[i]] > 1):
        c[a[i]] -= 1

print(ans)
