n = int(input())
ab = [map(int, input().split()) for _ in range(n-1)]
a, b = [list(i) for i in zip(*ab)]
# liの要素すべてが1になれば条件を満たす
li = [0] * n
ans = 'Yes'
root = 0
# ルートの検索
if(a[0] == a[1]):
    root = a[0]
elif(b[0] == b[1]):
    root = b[0]
elif(a[0] == b[1]):
    root = a[0]
elif(a[1] == b[0]):
    root = b[0]
# ルートがない場合はNo
if(root == 0):
    ans = 'No'
else:
    li[root-1] = 1
    for i in range(n-1):
        if(a[i] == root):
            li[b[i]-1] = 1
        elif(b[i] == root):
            li[a[i]-1] = 1
        else:
            break
    for i in range(n):
        if(li[i] == 0):
            ans = 'No'

print(ans)
