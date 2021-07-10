import sys
sys.setrecursionlimit(500*500)

n = int(input())
c = list(map(int, input().split()))

c.sort()
ans_pre = 0
ans_list = []


def count(list, b0):
    return b0 - len(list)


def f(a, b):
    if(len(b) == 1):
        ans_list.append(count(a, b[0]))
        return count(a, b[0])

    if(len(b) >= 2):
        ans_list.append(count(a, b[0]))
        a.append(b[0])
        b.pop(0)
        f(a, b)


a = []
f(a, c)
for i in range(len(ans_list)):
    if(i == 0):
        ans_pre = ans_list[i]
    else:
        ans_pre *= ans_list[i]

if(ans_pre == 0):
    ans = 0
else:
    ans = ans_pre % 1000000007
print(ans)
