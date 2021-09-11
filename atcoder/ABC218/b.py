p = list(map(int, input().split()))

li = []
for i in range(97, 123):
    li.append(chr(i))

for i in p:
    print(li[i-1], end="")
