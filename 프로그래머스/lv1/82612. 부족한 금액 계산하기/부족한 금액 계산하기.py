def solution(price, money, count):
    result = 0
    answer = 0
    for i in range(1, count+1):
        answer += price*i

    if answer >= money:
        return abs(answer-money)
    else:
        return 0
