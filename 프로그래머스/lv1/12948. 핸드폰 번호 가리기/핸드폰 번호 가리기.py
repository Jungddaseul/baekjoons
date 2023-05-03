def solution(phone_number):
    answer = ''
    len_number = len(phone_number)
    answer = '*' * (len_number - 4)
    answer += phone_number[-4:]
    return answer