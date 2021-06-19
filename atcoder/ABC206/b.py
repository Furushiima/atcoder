n = int(input())

i = 1
money = 0
while(1):
    money += i

    if(money >= n):
        break
    i += 1

print(i)
