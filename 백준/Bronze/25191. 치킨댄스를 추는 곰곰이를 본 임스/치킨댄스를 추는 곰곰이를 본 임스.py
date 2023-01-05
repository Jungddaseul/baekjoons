n = int(input())
a, b = map(int, input().split())
eat = a//2 + b

if n >= eat:
    print(eat)

else:
    print(n)
