ori = [1, 1, 2, 2, 2, 8]
num = list(map(int, input().split()))

for i in range(len(ori)):
    print(ori[i] - num[i], end= ' ')