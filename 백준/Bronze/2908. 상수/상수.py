n = list(map(str, input().split()))

a = "".join(reversed(n[0]))
b = "".join(reversed(n[1]))

print(max(a, b))