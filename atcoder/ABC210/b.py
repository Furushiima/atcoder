n = int(input())
s = input()
s = list(s)

loser = "Takahashi"
for i in range(n):
    if(int(s[i]) == 1):
        if(i % 2 == 1):
            loser = "Aoki"
        break

print(loser)
