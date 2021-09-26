a, b, c = map(int, input().split())
cc = c
fl = 0
for i in range(1000):
    if(a <= cc <= b):
        ans = cc
        fl = 1
        break
    else:
        cc += c

if(fl == 0):
    ans = -1

print(ans)
