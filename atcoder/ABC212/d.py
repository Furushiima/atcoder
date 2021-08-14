import heapq
n = int(input())
q = []
fukuro = []
add_sum = 0
for i in range(n):
    q.append([int(j) for j in input().split()])
    if(q[i][0] == 1):
        heapq.heappush(fukuro, q[i][1] - add_sum)
    elif(q[i][0] == 2):
        add_sum += q[i][1]
    else:
        print(heapq.heappop(fukuro) + add_sum)
