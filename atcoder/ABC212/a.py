a, b = map(int, input().split())

if((0 < a) & (b == 0)):
    ans = "Gold"
elif((a == 0) & (0 < b)):
    ans = "Silver"
elif((0 < a) & (0 < b)):
    ans = "Alloy"

print(ans)
