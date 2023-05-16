def solution(a, b, n):
    answer = 0
    # 1. 빈 병의 개수 n이 교환 가능한 최소 숫자 a 이상일 때까지 반복
    while n >= a:
        # 2. 현재 빈 병으로 받을 수 있는 새로운 개수 및 나머지 계산
        new_coke = n // a *b
        bottles = n % a
        
        # 3. 정답 반영 및 빈 병 개수 다시 계산
        answer += new_coke
        n = bottles + new_coke
    return answer