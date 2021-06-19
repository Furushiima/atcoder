import math

n = int(input())

money = math.floor(n*1.08)

if(money < 206):
    print("Yay!")

elif(money == 206):
    print("so-so")

elif(money > 206):
    print(":(")
