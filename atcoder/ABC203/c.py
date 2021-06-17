li = []
friend_number, money = map(int, input().split())
for i in range(friend_number):
    a = list(map(int, input().split()))
    li.append(a)
# [[1, 1, 1], [2, 2, 2], [3, 3, 3], ..., [n, n, n]]


friend_locate = 0
li.sort()

for i in range(friend_number):
    if (money >= li[friend_locate][0]):
        money += li[friend_locate][1]
        friend_locate += 1
    else:
        break

print(money)
