class Node:
    def __init__(self, num, move):
        self.num = num
        self.move = move
        self.prev = None
        self.next = None

def create_circular_dll(data):
    n = len(data)
    nodes = [Node(i + 1, move) for i, move in enumerate(data)]

    # 각 노드 연결 
    for i in range(n):
        nodes[i].prev = nodes[i-1]
        nodes[i].next = nodes[(i+1)%n]  # 마지막 노드에서 첫번째 노드는 +1로 안되니까 (+1)%n
    
    return nodes[0] # 첫번째 노드 반환

# 풍선 삭제 
def pop(node):
    if node.next == node:
        return None
    node.prev.next = node.next
    node.next.prev = node.prev
    return node.next    # 다음 노드 반환 

def solve(data):
    result = []
    curr = create_circular_dll(data)
    
    for i in range(len(data)):
        result.append(curr.num)
        move = curr.move
        curr = pop(curr)
        if curr is None:
            break
        # 이동 방향 (양수: 오른쪽, 음수: 왼쪽)
        if move > 0:
            for i in range(move-1): # 현재 위치에서 이미 1칸 이동했으므로 -1 
                curr = curr.next
        else:
            for i in range(-move):
                curr = curr.prev
    return result

# 입력 
n = int(input())
data = list(map(int, input().split()))
answer = solve(data)

# 출력 
print(' '.join(map(str, answer)))