def solution(n):
    # 0과 1은 소수가 아니므로 초기값을 2로 설정
    answer = 0
    
    # 주어진 범위 내의 숫자에 대해 소수 여부를 판별
    for num in range(2, n+1):
        is_prime = True
        
        # 2부터 현재 숫자의 제곱근까지 나누어 소수 여부 확인
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
                
        # 소수인 경우 answer 증가        
        if is_prime:
            answer += 1
    return answer