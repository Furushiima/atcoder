s = [input() for i in range(4)]

s.sort()
if((s[0] == "2B") & (s[1] == "3B") & (s[2] == "H") & (s[3] == "HR")):
    print("Yes")
else:
    print("No")
