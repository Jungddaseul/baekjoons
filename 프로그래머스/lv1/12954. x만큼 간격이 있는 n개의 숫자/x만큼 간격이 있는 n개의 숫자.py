def solution(x, n):
    answer = []
    result = x
    for _ in range(n):
        answer.append(result)
        result += x
        
    return answer