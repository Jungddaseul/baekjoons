n = int(input())
result = []

for _ in range(n):
    n = int(input())
    result.append(n)

for i in sorted(result):
    print(i)