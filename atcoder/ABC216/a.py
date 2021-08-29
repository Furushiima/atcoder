n = input()

n = n.split(".")
x = n[0]
y = int(n[1])

if(0 <= y <= 2):
    ans = x + "-"
elif(3 <= y <= 6):
    ans = x
else:
    ans = x + "+"

print(ans)
