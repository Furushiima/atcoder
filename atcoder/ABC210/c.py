from collections import Counter

n, k = map(int, input().split())
c = list(map(int, input().split()))

current_dict = Counter(c[0:k])
ans = len(current_dict)

for i in range(n-k):
    current_dict[c[i]] -= 1
    # ポップした結果なくなったものを削除
    if(current_dict[c[i]] == 0):
        current_dict.pop(c[i])

    # プッシュ処理
    if(c[i+k] in current_dict):
        current_dict[c[i+k]] += 1

    else:
        current_dict[c[i+k]] = 1

    ans = max(ans, len(current_dict))

print(ans)
