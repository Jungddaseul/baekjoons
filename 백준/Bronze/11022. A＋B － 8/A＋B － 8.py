n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    if 0 < a and b < 10:
        print(f'Case #{i+1}: {a} + {b} = {a+b}')
