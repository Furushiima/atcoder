n = input()
list_n = list(n)
list_n = [int(s) for s in list_n]


def plus_one(a):
    if(a == 9):
        return 0
    else:
        return a+1


if(list_n[0] == list_n[1] == list_n[2] == list_n[3]):
    ans = "Weak"
elif((plus_one(list_n[0]) == list_n[1]) & (plus_one(list_n[1]) == list_n[2]) & (plus_one(list_n[2]) == list_n[3])):
    ans = "Weak"
else:
    ans = "Strong"

print(ans)
