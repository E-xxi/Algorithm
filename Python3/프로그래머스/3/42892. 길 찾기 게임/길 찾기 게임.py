from collections import deque

class Node:
    def __init__(self,info, num, left = None,right=None):
        self.info = info #좌표
        self.num = num
        self.left = left
        self.right = right
    
    def has_left(self):
        return self.left is not None
    
    def has_right(self):
        return self.right is not None
    
def make_tree(nodeinfo):
    #nodes = {i+1 : nodeinfo[i] for i in range(len(nodeinfo))}
    #nodes_idx = list(sorted(node.items(), key = lambda x:(-x[1][1],-x[1][0])).keys())
    #책은 그냥 인덱스만 순서대로 정리함
    nodes= [i for i in range(1,len(nodeinfo)+1)]
    nodes.sort(key = lambda x: (nodeinfo[x-1][1], -nodeinfo[x-1][0]),reverse = True)

    
    root = None
    for i in range(len(nodes)):
        if root is None:
            root = Node(nodeinfo[nodes[0]-1],nodes[0])
        else:
            parent = root
            node = Node(nodeinfo[nodes[i]-1],nodes[i])
        
            while True: #트리에 삽입
                if node.info[0] < parent.info[0]: #작은건 왼쪽
                    if parent.has_left(): #채워져있으면 내려가
                        parent = parent.left
                        continue
                    parent.left = node
                    break
                else:
                    if parent.has_right():
                        parent = parent.right
                        continue
                    parent.right = node
                    break
    return root
                
def preorder(root): #본인 ->left->right
    answer = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        answer.append(node.num)
        stack.append(node.right)
        stack.append(node.left)
    
    return answer

def postorder(root): #왼->오->본인
    answer = []
    stack = [(root,False)]
    while stack:
        node,visited = stack.pop()
        if node is None:
            continue
        if visited:
            answer.append(node.num)
        else:
            stack.append((node,True))
            stack.append((node.right,False))
            stack.append((node.left,False))
        
        
    
    return answer
        

def solution(nodeinfo):
    # y값 비교(내림차순) x는 오름차순 정렬
     #이거 그대로 출력하면 중위순회
    root = make_tree(nodeinfo)
    return [preorder(root),postorder(root)]