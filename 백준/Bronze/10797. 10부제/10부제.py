day = int(input())
n = list(map(int, input().split()))
total = 0
for i in n:
    if day == i:
        total += 1
print(total)