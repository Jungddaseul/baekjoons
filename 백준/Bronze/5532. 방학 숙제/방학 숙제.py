L = int(input()) # 방학일 수
A = int(input()) # 총 국어 페이지
B = int(input()) # 총 수학 페이지
C = int(input()) # 하루 국어 최대 풀 수 있는 페이지
D = int(input()) # 하루 수학 최대 풀 수 있는 페이지

if (2 <= L <= 40) and (1 <= A) and (B <= 1000) and (1 <= C,D <= 100):
    kor_day = A // C
    if A % C != 0:
        kor_day += 1
    math_day = B // D
    if B % D != 0:
        math_day += 1
    day = L - (max(kor_day, math_day))
    print(day)