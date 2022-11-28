K, N, M = map(int, input().split())

total = K * N
if total > M:
    print(abs(total-M))
elif total <= M:
    print(0)