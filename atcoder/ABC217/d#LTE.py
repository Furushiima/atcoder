import bisect
l, q = map(int, input().split())
cx = [map(int, input().split()) for _ in range(q)]
c, x = [list(i) for i in zip(*cx)]

cut = []
cut_length = 0
count = 0


# 全体の長さ, 切られている箇所のリスト, 自分の位置が引数
# 返り値は, 自分の位置が含まれる部分の長さ
def f(l, cut, x):
    position = bisect.bisect(cut, x)
    if(position == 0):
        # 一度も切られていない場合
        if(cut_length == 0):
            length = l
        else:
            length = cut[0]
    elif(position == cut_length):
        length = l - cut[cut_length - 1]
    else:
        length = cut[position] - cut[position-1]

    return length


for cc in c:
    if(cc == 1):
        bisect.insort(cut, x[count])
        cut_length += 1
    else:
        length = f(l, cut, x[count])
        print(length)
    count += 1
