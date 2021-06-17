twon, road = map(int, input().split())
road_list = []

for i in range(road):
    a = list(map(int, input().split()))
    road_list.append(a)
# [[1, 1, 1], [2, 2, 2], [3, 3, 3], ..., [n, n, n]]

road_list.sort()
ans = 0
all_gone_list = []

# 町iからいけるi以外の町のリスト
def func(i, road_list):
    list = []
    for j in range(road):
        if(road_list[j][0] == i):
            if road_list[j][1] != i:
                list.append(road_list[j][1])
                list.append(func(road_list[j][1], road_list))

    return list


for i in range(twon):
    # この町からいける箇所のリスト
    gone_list = func(i, road_list)
    ans += len(gone_list)

print(ans)


