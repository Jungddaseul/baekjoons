l, p = map(int, input().split())
news = list(map(int, input().split()))
ans = []

if (1 <= l <= 10) and (1 <= p <= 1000):
    sang = l * p
    for i in news:
        ans.append(i - sang)

for i in ans:
    print(i, end=' ')