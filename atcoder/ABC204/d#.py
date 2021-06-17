n = int(input())
li = list(map(int, input().split()))
# 2つのオーブン
a = 0
b = 0
j = 0
ans = 0

li.sort(reverse=True)

for i in range(n):
    if(a > b):
        b += li[j]
    else:
        a += li[j]
    j += 1

if(a >= b):
    ans = a
else:
    ans = b

print(ans)
