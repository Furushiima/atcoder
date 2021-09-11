n = int(input())
s = []
t = []
ans = "No"
for i in range(n):
    ss = input()
    s.append(ss)

for i in range(n):
    tt = input()
    t.append(tt)


# 時計周りに90度回転
def rotate(li):
    temp_li = []
    rotated_li = []
    temp_str = ""
    # 上下反転
    for i in range(n):
        i += 1
        temp_li.append(li[-i])
    # 行と列の入れ替え
    for i in range(n):
        for j in range(n):
            temp_str += temp_li[j][i]
        rotated_li.append(temp_str)
        temp_str = ""
    
    return rotated_li


# 判定
def judge(li_a, li_b):
    # li_aから図形抽出
    flag = 0
    tyouten_a = [0,0]
    li_a_zukei = []
    for i in range(n):
        for j in range(n):
            if((flag == 1) & (li_a[i][j] == "#")):
                li_a_zukei.append(int(str(j - tyouten_a[1]) + str(i - tyouten_a[0])))
            elif(li_a[i][j] == "#"):
                tyouten_a[0] = i
                tyouten_a[1] = j
                flag = 1
            else:
                pass
    
    # li_bから図形抽出
    flag = 0
    tyouten_b = [0,0]
    li_b_zukei = []
    for i in range(n):
        for j in range(n):
            if((flag == 1) & (li_b[i][j] == "#")):
                li_b_zukei.append(int(str(j - tyouten_b[1]) + str(i - tyouten_b[0])))
            elif(li_b[i][j] == "#"):
                tyouten_b[0] = i
                tyouten_b[1] = j
                flag = 1
            else:
                pass
    
    # 比較
    if(li_a_zukei == li_b_zukei):
        return True
    else:
        return False


# 3回回転して比較
for i in range(4):
    if(judge(s, t)):
        ans = "Yes"
    if(i == 3):
        break
    else:
        t = rotate(t)
print(ans)
