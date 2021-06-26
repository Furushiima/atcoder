n = int(input())
kukan = []
for i in range(n):
    a = list(map(int, input().split()))
    kukan.append(a)
# [[1, 1, 1], [2, 2, 2], [3, 3, 3], ..., [n, n, n]]

all_kukan = []
ans = 0

for i in range(n):

    # 比較する区間
    new_kukan = []

    # [1,9] -> [1,9]
    if(kukan[i][0] == 1):
        new_kukan.append(kukan[i][1])
        new_kukan.append(kukan[i][2])

    if(kukan[i][0] == 2):
        new_kukan.append(kukan[i][1])
        new_kukan.append(kukan[i][2]-0.1)

    if(kukan[i][0] == 3):
        new_kukan.append(kukan[i][1]+0.1)
        new_kukan.append(kukan[i][2])

    if(kukan[i][0] == 4):
        new_kukan.append(kukan[i][1]+0.1)
        new_kukan.append(kukan[i][2]-0.1)

    for j in range(int(len(all_kukan)/2)):
        if(max(all_kukan[(2*j-1)-1], new_kukan[0]) <= min(all_kukan[(2*j)-1], new_kukan[1])):
            ans += 1

    all_kukan.extend(new_kukan)

print(ans)
