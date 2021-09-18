s1 = input()
s2 = input()
s3 = input()
t = input()
li = list(t)
ans = ""
for q in li:
    if(q == "1"):
        ans += s1
    elif(q == "2"):
        ans += s2
    else:
        ans += s3
print(ans)
