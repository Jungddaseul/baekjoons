def solution(n):
    answer = 0
    root = n ** 0.5
    
    if root == int(root):
        return (int(root) + 1) ** 2
    else:
        return -1