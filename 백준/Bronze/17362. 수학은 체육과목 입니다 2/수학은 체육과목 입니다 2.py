n = int(input())
ans = n % 8

if ans == 1:
    print(1)
elif ans in [2, 0]:
    print(2)
elif ans in [3, 7]:
    print(3)
elif ans in [4, 6]:
    print(4)
elif ans == 5:
    print(5)