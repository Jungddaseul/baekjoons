from itertools import combinations

def solution(number):
    answer = 0
    result = 0
    combinations_lst = list(combinations(number, 3))
    
    for i in combinations_lst:
        if sum(i) == 0:
            result += 1

    return result