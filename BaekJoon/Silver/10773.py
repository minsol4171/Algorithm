import sys

def stack(nums):
    st = []
    for num in nums:
        if num != 0:
            st.append(num)
        else:
            st.pop()
    
    return sum(st)

def main():
    # 입력 
    input = sys.stdin.readline
    k = int(input())
    nums = [int(input()) for i in range(k)]
    
    # 연산 
    result = stack(nums)

    # 출력 
    print(result)

if __name__=="__main__":
    main()