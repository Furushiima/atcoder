n = int(input())
for i in range(61):
    if(2**i>n):
        ans = i-1
        break

print(ans)
