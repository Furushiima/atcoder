n, m = map(int, input().split())
a = list(map(int, input().split()))

a_set = set(a)
yakusuu_set = set(a)
ans = []
for i in a_set:
    for j in range(317):
        k = j+1
        if(i % k == 0):
            yakusuu_set.add(k)
            yakusuu_set.add(i//k)
        if(i == k):
            break

for i in range(m):
    i = i+1
    flg = 0
    for j in yakusuu_set:
        if(j == 1):
            continue
        if(i % j == 0):
            flg = 1
            break
    if(flg == 0):
        ans.append(i)

print(len(ans))
for i in ans:
    print(i)
