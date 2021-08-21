import itertools
s, k = input().split()
k = int(k)
sorted_set = set(list(itertools.permutations(s)))
sorted_list = list(sorted_set)
sorted_list.sort()
ans = ''.join(sorted_list[k-1])
print(ans)
