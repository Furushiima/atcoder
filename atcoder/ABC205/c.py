a, b, c = map(int, input().split())

if c % 2 == 0:
    # cが偶数の時
    if (abs(a) > abs(b)):
        ans = ">"
    elif (abs(a) < abs(b)):
        ans = "<"
    elif (abs(a) == abs(b)):
        ans = "="
else:
    # cが奇数の時
    if (a > b):
        ans = ">"
    elif (a < b):
        ans = "<"
    elif (a == b):
        ans = "="

print(ans)
