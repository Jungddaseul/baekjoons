def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        n = (len(s) // 2)-1
        return s[n:n+2]    

    else:
        n = (len(s) // 2)
        return(s[n])
