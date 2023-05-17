def solution(nums):
    choose = len(nums) / 2
    set_nums = set(nums)
    answer = min(len(set_nums), choose)
    return answer