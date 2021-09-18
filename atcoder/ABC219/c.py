x = input()
n = int(input())
s = []
dic1 = {}
dic2 = {}
alpha = [chr(j) for j in range(97, 97+26)]
ans = []
for i in range(26):
    dic1[x[i]] = alpha[i]
    dic2[alpha[i]] = x[i]

for _ in range(n):
    name = input()
    newname = ""
    for c in name:
        newname += dic1[c]
    s.append(newname)
s = sorted(s)
for newname in s:
    orgname = ""
    for c in newname:
        orgname += dic2[c]
    ans.append(orgname)
for a in ans:
    print(a)
