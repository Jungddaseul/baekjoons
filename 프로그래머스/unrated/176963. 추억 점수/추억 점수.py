def solution(name, yearning, photo):
    answer = []
    dict1 = {}
    # 딕셔너리 만들기
    for i in range(len(name)):
        dict1[name[i]] = yearning[i]
    
    # photo 이중리스트에서 값 비교하기
    for people in photo:
        result = 0
        # print(people)
        for person in people:
            # print(person)
            if person in name:
                result += dict1[person]
        answer.append(result)

    return answer
