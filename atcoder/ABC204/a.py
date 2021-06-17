a, b = map(int, input().split())

if(a == b):
    ans = a
else:
    if(a+b == 1):
        ans = 2
    elif(a+b == 2):
        ans = 1
    else:
        ans = 0

print(ans)
