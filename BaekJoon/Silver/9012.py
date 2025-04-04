import sys

def validPS(strings):
    result = []
    
    for line in strings:
        stack = []
        is_valid = True
        
        for ch in line:
            # '('가 나오면 스택에 넣고  
            if ch == '(':   
                stack.append(ch)
            # ')'가 나오면 스택에서 '('를 꺼냄 
            elif ch == ')':
                if stack:
                    stack.pop()
                # 스택이 비어있는데 )가 나오면 잘못된 vps
                else:
                    is_valid = False
                    break
        # 끝났을때 스택이 비어있지 않으면 잘못된 vps
        if stack:
            is_valid = False
        result.append('YES' if is_valid else 'NO') 
               
    return result
        

def main():
    # 입력 
    input = sys.stdin.readline
    t = int(input())
    strings = [input().strip() for i in range(t)]
    
    # 연산 
    result = validPS(strings)

    # 출력 
    print('\n'.join(result))

if __name__=="__main__":
    main()