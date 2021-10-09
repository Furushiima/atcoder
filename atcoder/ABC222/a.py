ans = input()

while (len(ans) <= 3):
    ans = "0" + ans
    if(len(ans) == 4):
        break

print(ans)

