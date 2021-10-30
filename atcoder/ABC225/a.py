s = input()
same = 0
if(s[0] == s[1]):
    same += 1
if(s[1] == s[2]):
    same += 1
if(s[0] == s[2]):
    same += 1

if(same == 0):
    ans = 6
elif(same == 1):
    ans = 3
else:
    ans = 1

print(ans)
