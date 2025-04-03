def simulate_wheel(n, rotations):
    """회전 정보를 바탕으로 바퀴에 적어놓은 알파벳을 알아낸다."""
    wheel = ['?']* n
    used = set()
    curr = 0
    
    for s, ch in rotations:
        curr = (curr+s)%n
        if wheel[curr] == '?':  # 칸이 비어있을 때 
            if ch in used:
                return "!"  # 다른 칸에 이미 같은 문자가 있으면 X 
            wheel[curr] = ch
            used.add(ch)
        elif wheel[curr] != ch: # 칸에 이미 다른 문자가 있으면 X
            return "!"  
    
    result = []
    for i in range(n):
        result.append(wheel[(curr - i)%n])  # 마지막에 가리킨 문자부터 시계방향 출력 

    return ''.join(result)
    
      
def main():
    # 입력 
    n, k = map(int, input().split())
    rotations = []
    for i in range(k):
        s, ch = input().split()
        s = int(s)
        rotations.append((s, ch))
    
    # 연산 
    result = solve(n, rotations)

    # 출력 
    print(result)

if __name__=="__main__":
    main()