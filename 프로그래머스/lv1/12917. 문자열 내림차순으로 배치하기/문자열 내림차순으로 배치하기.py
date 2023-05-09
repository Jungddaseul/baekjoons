def solution(s):
    answer = list(s)
    result = ''.join(sorted(answer, reverse=True))

    return result