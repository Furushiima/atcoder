a = list(map(str, input().split()))
b = sorted(a)
ans = 'Yes'
if(a[0] != b[0]):
    ans = 'No'
print(ans)
