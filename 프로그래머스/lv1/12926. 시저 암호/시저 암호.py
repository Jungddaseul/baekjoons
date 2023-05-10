def solution(s, n):
    s_lis = list(s)
    for i in range(len(s)):
        if s_lis[i].isupper():
            s_lis[i] = chr((ord(s_lis[i]) - ord('A') + n) % 26 + ord('A'))
        elif s_lis[i].islower():
            s_lis[i] = chr((ord(s_lis[i]) - ord('a') + n) % 26 + ord('a'))

    return ''.join(s_lis)
