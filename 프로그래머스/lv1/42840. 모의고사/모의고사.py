def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    
    # 맞춘 개수를 확인하는 코드
    for i in range(len(answers)):
        # 첫 번째
        if answers[i] == a[i%5]:
            score[0] += 1
        # 두 번째
        if answers[i] == b[i%8]:
            score[1] += 1
        
        # 세 번째
        if answers[i] == c[i%10]:
            score[2] += 1
            
    result = max(score)  # 가장 많이 맞춘 사람의 개수
    
    for i in range(len(score)):
        if score[i] == result:
            answer.append(i+1)
        
    return answer