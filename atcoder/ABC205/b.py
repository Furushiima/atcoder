n = int(input())
a = input().split()
ans = "Yes"

# リストに重複した要素があるか判定
def has_duplicates(seq):
    return len(seq) != len(set(seq))


if has_duplicates(a):
    ans = "No"

print(ans)
