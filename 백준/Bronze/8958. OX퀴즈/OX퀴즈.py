n = int(input())

for _ in range(n):
    a = list(input())
    result = []
    cnt = 0

    for i in a:
        if i == 'O':
            cnt += 1
            result.append(cnt)
        if i == 'X':
            cnt = 0
            
    print(sum(result))