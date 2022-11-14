while True:
    try:
        a, b = map(int, input().split())
        0 < a and b < 10
        print(a+b)
    except:
        break