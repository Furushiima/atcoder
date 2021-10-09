n, m = map(int, input().split())
a = [["w"]*m]*(2*n)
player_dict_list = []

for i in range(2*n):
    s = list(map(str, input().split()))
    a[i] = s[0]
    dict = {}
    dict["index"] = i
    dict["win"] = 0
    player_dict_list.append(dict)


# s1が勝つとwin, 負けるとlose, 引き分けはdrawを返す
def janken(s1, s2):
    if(s1 == s2):
        return "draw"
    elif((s1 == "P") & (s2 == "C") | (s1 == "G") & (s2 == "P") | (s1 == "C") & (s2 == "G")):
        return "lose"
    else:
        return "win"


for i in range(m):
    player_dict_list = sorted(
        player_dict_list, key=lambda x: (x['win'], -x["index"]), reverse=True)
    # じゃんけん
    for j in range(n):
        player1 = player_dict_list[j*2]["index"]
        player2 = player_dict_list[j*2 + 1]["index"]
        result = janken(a[player1][i], a[player2][i])
        if(result == "win"):
            player_dict_list[j*2]["win"] += 1
        if(result == "lose"):
            player_dict_list[(j*2 + 1)]["win"] += 1


player_dict_list = sorted(
    player_dict_list, key=lambda x: (x['win'], -x["index"]), reverse=True)
for d in player_dict_list:
    print(d["index"]+1)
