s = [input() for i in range(3)]

contests = ["ABC", "ARC", "AGC", "AHC"]
for contest in s:
    if(contest == "ABC"):
        contests[0] = "0"
    elif(contest == "ARC"):
        contests[1] = "0"
    elif(contest == "AGC"):
        contests[2] = "0"
    elif(contest == "AHC"):
        contests[3] = "0"

for i in contests:
    if(i == "0"):
        pass
    else:
        ans = i
print(ans)
