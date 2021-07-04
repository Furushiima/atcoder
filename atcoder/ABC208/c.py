n, k = map(int, input().split())
a = list(map(int, input().split()))

base = k // n
mod = k % n

b = a
b = sorted(a)

# 1個多くもらえる最低の国民番号
border = b[mod-1]

for i in range(len(a)):
    if(mod == 0):
        print(base)
    elif(a[i] <= border):
        print(base+1)
    else:
        print(base)
