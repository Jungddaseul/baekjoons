def solution(n, m):
    answer = 0
    result = []
    for i in range(min(n,m), 0, -1):
        if (n % i) == 0 and (m % i == 0):
            GCD = i
            result.append(GCD)
            break
    
    for i in range(max(n,m), (n*m)+1):
        if (i % n == 0) and (i % m == 0):
            LCM = i
            result.append(LCM)
            break
    return result