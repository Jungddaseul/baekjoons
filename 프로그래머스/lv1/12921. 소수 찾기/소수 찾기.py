def solution(n):
    if n < 2:
        return 0

    # 주어진 범위 내의 숫자에 대해 소수 여부를 판별하는 리스트
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # 2부터 숫자의 제곱근까지 소수 여부를 판별
    for num in range(2, int(n ** 0.5) + 1):
        if is_prime[num]:
            # num의 배수들은 소수가 아님
            for i in range(num * num, n + 1, num):
                is_prime[i] = False

    return sum(is_prime)