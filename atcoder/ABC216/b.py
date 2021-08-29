n = int(input())
st = [map(str, input().split()) for _ in range(n)]
s, t = [list(i) for i in zip(*st)]
m = n
ans = "No"
flag = False
for i in range(n):
    m -= 1
    for j in range(m):
        j += (i+1)
        if(s[i] == s[j]):
            if(t[i] == t[j]):
                flag = True
                break
    
    if(flag):
        ans = "Yes"
        break

print(ans)
