a, b, c, d = map(int,input().split())

water = a
red = 0
ans = 0

# 傾きで判定
if(b >= c*d):
    ans = -1
else:
    while(1):
        ans += 1
        water += b
        red += c
        if(water <= d*red):
            break

print(ans)
