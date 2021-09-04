n = int(input())
p = list(map(int, input().split()))
q = []
# q = [0,0,0,0,0,...]
for i in range(n):
    q.append(0)
count = 1
for i in p:
    q[i-1] = count
    count += 1
for ans in q:
    print(ans, end=" ")
