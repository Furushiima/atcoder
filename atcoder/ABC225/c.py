n, m = map(int, input().split())

b = [0]*n
c = [[0]*m]*n
for i in range(n):
    b[i] = list(map(int, input().split()))
ans = 'Yes'

# ひとつ右側の数字が1大きいかのチェック
for i in range(n):
    for j in range(m-1):
        if((b[i][j]+1) != b[i][j+1]):
            ans = 'No'
# ひとつ下の数字が7大きいかのチェック
for i in range(n-1):
    for j in range(m):
        if((b[i][j]+7) != b[i+1][j]):
            ans = 'No'
# 行列をすべて7で割った余りに変換する(割り切れる場合は7に変換)
for i in range(n):
    for j in range(m):
        if((b[i][j] % 7) == 0):
            b[i][j] = 7
        else:
            b[i][j] = b[i][j] % 7
# すべての行が等しいかチェック
for i in range(n-1):
    if(b[i] != b[i+1]):
        ans = 'No'
# ひとつ右側の数字が1大きいかのチェック
for i in range(m-1):
    if((b[0][i] + 1) != b[0][i+1]):
        ans = 'No'

print(ans)
