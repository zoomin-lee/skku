'''
1. 그래프의 용어
- 정점 = vertex
- 간선 = edge
- 그래프 G = (V,E)

2. 정의
- 경로 : 시작 정점으로부터 도착 정점에 이르기까지의 정점들을 나열하여 표현
- 단순 경로 : 모두 다른 정점으로 구성된 경로
- 싸이클 : 시작 정점과 도착 정점이 동일한 단순 경로
- 부분그래프 : 주어진 그래프의 정점과 간선의 일부분으로 이루어진 그래프
- 신장트리 : 그래프의 모든 정점들을 싸이클 없이 연결하는 부분그래프
- 실세계의 그래프는 정점의 평균 차수가 작은 희소그래프이므로 그래프를 표현할 떄 주로 인접 리스트를 사용
'''

class Node :
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def enqueue(self, item):
        temp = Node(item)
        if self.is_empty():
            self.head = temp
            temp.next = temp
        else :
            temp.next = self.head.next
            self.head.next=temp
            self.head=temp

    def dequeue(self):
        if self.is_empty():
            return None
        else :
            temp = self.head.next
            if temp == temp.next:
                self.head = None
            else :
                self.head.next = temp.next
        return temp.item

# DFS : 깊이우선탐색
adj_list =[[2,1], [3,0], [3,0], [9,8,2,1], [5], [7,6,4], [7,5], [6,5], [3], [3]]
N = len(adj_list)
visited = [False] * N

def dfs(v):
    visited[v] = True
    print(v, ' ', end='')
    for i in adj_list[v]:
        if not visited[i]:
            dfs(i)

print("DFS 방문 순서 : ")
for i in range(N):
    if not visited[i]:
        dfs(i)

# BFS : 너비우선탐색
def bfs(v): #o(간선+정점)
    queue = Queue()
    visited[v] = True
    queue.enqueue(v)

    while not queue.is_empty():
        v = queue.dequeue()
        print(v, ' ', end='')
        for i in adj_list[v]:
            if not visited[i]:
                visited[i] = True
                queue.enqueue(i)

adj_list =[[2,1], [3,0], [3,0], [9,8,2,1], [5], [7,6,4], [7,5], [6,5], [3], [3]]
N = len(adj_list)
visited = [False] * N

print("\nBFS 방문 순서 : ")
for i in range(N):
    if not visited[i]:
        bfs(i)