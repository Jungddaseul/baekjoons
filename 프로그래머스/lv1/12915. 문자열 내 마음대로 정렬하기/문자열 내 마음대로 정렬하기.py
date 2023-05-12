def solution(strings, n):
    answer = []
    new_s = []
    
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i] # 추출한 문자열을 앞으로 보냄 
        new_s.append(strings[i])
        
    for w in sorted(new_s):
        answer.append(w[1:])

    return answer