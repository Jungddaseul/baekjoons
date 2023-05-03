def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            return '김서방은 %i에 있다' %i
    return answer