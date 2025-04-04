import sys

def is_balanced(strings):
    result = []
    
    for line in strings:
        stack = []
        is_valid = True
        
        for ch in line:
            # '('가 나오면 스택에 넣고  
            if ch == '(' or ch == '[':   
                stack.append(ch)
            # ')'가 나오면 스택에서 '('를 꺼냄 
            elif ch == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                # 스택이 비어있는데 )가 나오면 잘못된 vps
                else:
                    is_valid = False
                    break
            elif ch == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    is_valid = False
                    break 
                
        # 끝났을때 스택이 비어있지 않으면 잘못된 vps
        if stack:
            is_valid = False
        result.append('yes' if is_valid else 'no') 
               
    return result
        

def main():
    # 입력 
    input = sys.stdin.readline
    strings = []
    while True:
        line = input().rstrip()
        if line=='.':
            break
        strings.append(line)
    
    # 연산 
    result = is_balanced(strings)

    # 출력 
    print('\n'.join(result))

if __name__=="__main__":
    main()