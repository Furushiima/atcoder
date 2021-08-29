n = int(input())
ans = []


def magic(x):
    if(x == 0):
        ans.insert(0, "B")
        return 0
    elif(x == 1):
        ans.insert(0, "A")
        return 0
    elif((x % 2) == 1):
        ans.insert(0, "A")
        return x-1
    else:
        ans.insert(0, "B")
        return x//2


for i in range(120):
    n = magic(n)

print(''.join(ans))
