a, b = map(int, input().split())
c = 2 * int(input())

if(a + b-c >= 0):
    print(a + b - c)
else:
    print(a + b)