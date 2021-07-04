a, b = map(int, input().split())

if a <= b <= a*6:
    ans = "Yes"
else:
    ans = "No"

print(ans)
