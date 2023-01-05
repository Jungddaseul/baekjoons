def solution(k, score):
    answer = []
    present = []
    
    for i in score:
        if len(present) < k:
            present.append(i)
        else:
            if min(present) < i:
                present.remove(min(present))
                present.append(i)
        answer.append(min(present))
    return answer