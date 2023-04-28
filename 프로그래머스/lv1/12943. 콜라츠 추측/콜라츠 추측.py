def solution(num):
    cnt = 0
    
    for _ in range(500):
        
        if num == 1:
            break
            
        if num % 2 == 0:
            num /= 2
            cnt += 1
        else:
            num = num * 3 + 1
            cnt += 1
        
    if num != 1:
        return -1

    return cnt