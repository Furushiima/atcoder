k = int(input())
a, b = map(str, input().split())


def Base_n_to_10(X, n):
    out = 0
    for i in range(1, len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out


a_10 = Base_n_to_10(a, k)
b_10 = Base_n_to_10(b, k)
ans = a_10 * b_10
print(ans)
