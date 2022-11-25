for _ in range(3):
    h, m, s, h1, m1, s1 = map(int, input().split())
    h2 = h1 - h
    m2 = m1 - m
    s2 = s1 - s
    if s2 < 0:
        s2 %= 60
        m2 -= 1
    if m2 < 0:
        m2 %= 60
        h2 -= 1
    print(h2, m2, s2)