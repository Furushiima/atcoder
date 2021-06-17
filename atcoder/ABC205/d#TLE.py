n, q = map(int, input().split())
a = list(map(int, input().split()))
k = [int(input()) for i in range(q)]

# aの補集合っぽいやつ 
b = []
i = 0
a_i = 0

while True:
    if(i+1 == a[a_i]):
        a_i += 1
        if(a_i == len(a)):
            break
    else:
        b.append(i+1)
    i += 1

for i in k:
    if(i > len(b)):
        print((a[-1] + (i - len(b))))
    else:
        print(b[i-1])
