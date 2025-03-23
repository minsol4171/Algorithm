def solution(array):
    idx = [0] * (max(array)+1)    # 숫자의 출연 횟수를 세는 리스트
    
    for i in array:
        idx[i] += 1 # 등장할 때마다 +1
        
    if idx.count(max(idx)) > 1: # 최빈값이 여러개인 경우
        return -1
    else:
        return idx.index(max(idx))