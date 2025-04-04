def stack(commands):
    stack = []
    result = []
    
    for command in commands:
        if command[0] == '1':
            stack.append(int(command[1]))
        elif command[0] == '2':
            result.append(str(stack.pop()) if stack else '-1')
        elif command[0] == '3':
            result.append(str(len(stack)))
        elif command[0] == '4':
            result.append('1' if not stack else '0')
        elif command[0] == '5':
            result.append(str(stack[-1]) if stack else '-1')
    
    return result
    
def main():
    # 입력 
    n = int(input())
    commands = [input().strip().split() for i in range(n)]
    
    # 연산 
    result = stack(commands)

    # 출력 
    print('\n'.join(result))

if __name__=="__main__":
    main()