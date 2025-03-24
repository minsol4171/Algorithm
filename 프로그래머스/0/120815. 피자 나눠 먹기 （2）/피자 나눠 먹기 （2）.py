def solution(n):
    i = 1
    while True:
        if i*n % 6 == 0:
            return i*n // 6
        i+=1