def solution(n):
    answer = []
    for i in str(n):
        answer.append(i)
        a = reversed(answer)
    return list(map(int, a))