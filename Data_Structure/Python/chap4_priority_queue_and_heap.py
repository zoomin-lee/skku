'''
1. 우선 순위 큐( Priority Queue )
: 임의의 기준을 중심으로 가장 높은 우선순위를 가지는 항목의 삭제 및 반환과 임의의 우선순위를 가지는 항목 삽입을 지원하는 자료구조
- stack : 시간 중심으로 가장 마지막에 삽입된 항목이 가장 높은 우선순위를 가짐
- queue : 시간 중심으로 가장 처음에 삽입된 항목이 가장 높은 우선순위를 가짐

(1) 시간 복잡도 비교
                                enqueue         dequeue
-------------------------------------------------------------
list                            o(1)            o(n)
sorted list                     o(n)            o(1)
sorted linked list              o(n)            o(1)
sorted circular linked list     o(n)            o(1)
unsorted circular linked list   o(1)            o(n)
heap                            o(log n)        o(log n)

(2) heap을 이용한 구현
- 동기 : 우선순위가 가장 높은 항목을 삭제 및 반환할 경우, 모든 항목을 정렬시킬 필요가 없음
- heap : 완전 이진 트리로서 힙 속성을 만족시키는  자료 구조  -> 리스트로 구성해도 자리 낭비 없음
- 힙 속성 (heap property) = 힙 조건 : 부모 노드 키 값의 우선수위가 자식 노드 키 값의 우선순위보다 높음
- 힙의 종류 : Max 힙( 루트 노드의 키가 가장 큼 ), Min 힙( 루트 노드의 키가 가장 작음 )
- 단말 노드의 인덱스 값 : 노드의 개수가 n개 일 때, n//2 ~ n-1

1) heapify ( 리스트를 힙으로 만들기 )
- 하향식(top-down) 알고리즘 : list에 각 항목(n개)을 빈 힙에 삽입(insert o(log n)) = o(n log n)
- 상향식(bottom-up) 알고리즘 : list를 이진 트리로 간주하고, 마지막 비단말 노드(n//2-1)을 시작으로 루트 노드까지의
                            각 노드를 루트 노드로 하는 서브 트리에 대해서 downheap() 사용하여 힙 속성을 충족시킴
                            ( 수행 순서 : 왼쪽 -> 오른쪽, 아래 -> 위 ) o(n)

2) 완전 이진 트리 : 마지막 레벨을 제외한 레벨의 노드는 모두 차있고, 마지막 레벨 노드는 왼쪽부터 빠짐없이 채워진 노드
- 높이가 h인 완전이진트리에 존재하는 노드의 수 : 2^h ~ 2^(h+1)-1
- h = 올림(log2(n+1)) - 1
'''

# 정렬된 리스트
class list_priorityqueue :
    def __init__(self):
        self.priority_list = []

    def enqueue(self, item):
        index = 0
        for i in range(len(self.priority_list)):
            if self.priority_list[i] < item:
                index = i+1
        self.priority_list.insert(index, item)

    def dequeue(self):
        self.priority_list.pop()

    def print_list(self):
        print(self.priority_list)

# 정렬된 단순 연결 리스트 : 작을수록 우선순위가 높다면 오름차순
class Node:
    def __init__(self, item):
        self.key = item
        self.next = None

class linked_PriorityQueue :
    def __init__(self):
        self.head = None

    def enqueue(self, item): #탐색 o(n)+ 삽입 o(1)
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.item > item:
                stop = True
            else :
                previous = current
                current = current.next
        temp = Node(item)

        if previous == None:
            temp.next = self.head
            self.head = temp
        else :
            temp.next = current
            previous.next = temp

    def dequeue(self):
        if self.head == None:
            return None
        else:
            temp = self.head
            dequeue_item = temp.item
            self.head = self.head.next
            return dequeue_item

# 환형연결리스트로 구현
class CList_priorityqueue :
    def __init__(self):
        self.head = None # 마지막 노드

    def is_empty(self):
        return self.head == None

    def enqueue(self, item):
        temp = Node(item)
        if self.is_empty():
            temp.next = temp
            self.head = temp
        else:
            temp.next = self.head.next
            self.head.next = temp

    def dequeue(self):
        temp = self.head.next
        current = temp
        max = current.key
        while True :
            if max < current.next.key:
                max = current.next.key
                delete_node = current.next
                previous = current
            current = current.next
            if current != temp :
                continue
            else :
                previous.next = delete_node.next
                break

    def print_list(self):
        temp = self.head.next
        current = temp
        while True:
            print(current.key, end=' ')
            current = current.next
            if current != temp:
                continue
            else:
                break
        print()

# Min heap
class Binaryminheap :
    def __init__(self, array=[]): # o(1)
        self.items = array

    def size(self): # o(1)
        return len(self.items)

    def swap(self, i, j): # o(1)
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def insert(self,key): # o(log n) : 최악의 경우 힙의 높이 h = 올림log(n+1)-1 만큼 upheap
        self.items.append(key)
        self.upheap(self.size()-1)

    def extract_min(self): # o(log n) : 최악의 경우 힙의 높이 h = 올림log(n+1)-1 만큼 downheap
        if self.size() == 0:
            print("heap is empty")
            return None
        minimum = self.items[0]
        self.swap(0,-1)
        del self.items[-1]
        self.downheap(0)
        return minimum

    def downheap(self, i):
        while 2*i + 1 <= self.size()-1:
            k = 2*i+1
            if k < self.size()-1 and self.items[k] > self.items[k+1]:
                k += 1
            if self.items[i] < self.items[k]:
                break
            self.swap(i, k)
            i = k

    def upheap(self, i):
        while i > 0 and self.items[(i-1//2)] < self.items[i]:
            self.swap(i, (i-1)//2)
            i = (i-1) // 2

    def heapify(self, array): #o(n)
        for i in range(len(array)//2-1, -1, -1):
            self.downheap(i)

    def print_heap(self):
        for i in range(0,self.size()):
            print(self.items[i], end = ' ')
        print("\nsize of heap = ", self.size())

# Max heap
class Binarymaxheap :
    def __init__(self, array=[]): # o(1)
        self.items = array

    def size(self): # o(1)
        return len(self.items)

    def swap(self, i, j): # o(1)
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def insert(self,key): # o(log n) : 최악의 경우 힙의 높이 h = 올림log(n+1)-1 만큼 upheap
        self.items.append(key)
        self.upheap(self.size()-1)

    def extract_max(self): # o(log n) : 최악의 경우 힙의 높이 h = 올림log(n+1)-1 만큼 downheap
        if self.size() == 0:
            print("heap is empty")
            return None
        maxmum = self.items[0]
        self.swap(0,-1)
        del self.items[-1]
        self.downheap(0)
        return maxmum

    def downheap(self, i):
        while 2*i + 1 <= self.size()-1:
            k = 2*i+1
            if k < self.size()-1 and self.items[k] < self.items[k+1]:
                k += 1
            if self.items[i] > self.items[k]:
                break
            self.swap(i, k)
            i = k

    def upheap(self, i):
        while i > 0 :
            parent_index = (i-1) // 2
            if self.items[parent_index] < self.items[i] :
                self.swap(i, (i-1)//2)
                i = (i-1) // 2
            else :
                break

    def heapify(self, array): #o(n)
        for i in range(len(array)//2-1, -1, -1):
            self.downheap(i)

    def print_heap(self):
        for i in range(0,self.size()):
            print(self.items[i], end = ' ')
        print("\nsize of heap = ", self.size())

if __name__ == '__main__':
    array = [3,2,4,9,5,8,6]
    minheap = Binarymaxheap(array)
    minheap.heapify(array)
    minheap.print_heap()
    minheap.insert(11)
    minheap.print_heap()
    minheap.insert(10)
    minheap.print_heap()
    print(minheap.extract_max())
    minheap.print_heap()
