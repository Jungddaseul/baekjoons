def solution(name, yearning, photo):
    answer = []
    dict1 = {}
    for i in range(len(name)):
        dict1[name[i]] = yearning[i]
    
    for peple in photo:
        result = 0
        for person in peple:
            if person in name:
                result += dict1[person]
        answer.append(result)
    return answer