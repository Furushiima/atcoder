n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

i_a = 0
i_b = 0
min = abs(a[i_a] - b[i_b])
while(1):
    if(a[i_a] > b[i_b]):
        dif = abs(a[i_a] - b[i_b])
        if(min > dif):
            min = dif
        i_b += 1

    else:
        dif = abs(a[i_a] - b[i_b])
        if(min > dif):
            min = dif
        i_a += 1

    if((i_a == n) | (i_b == m)):
        break

print(min)



