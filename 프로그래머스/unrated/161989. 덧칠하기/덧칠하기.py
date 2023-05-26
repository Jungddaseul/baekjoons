def solution(n, m, section):
    answer = 0
    painted = 0
    
    for value in section:
        if value >= painted:
            painted = value + m
            answer += 1
            
    return answer