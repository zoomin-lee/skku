'''
(1) Stack
- Last in Frist out
- Top에서만 삽입/삭제가 이루어지는 list
- list로 구현했을 때 pop/push의 시간복잡도 : O(1)
- singly linked list로 구현했을 때 pop/push의 시간복잡도 : O(1)

(2) Queue
- Frist in Frist out
- list로 구현했을 때 enqueue : O(1), dequeue : O(n)
- singly linked list enqueue : O(n), dequeue : O(1)
- circular linked list enqueue : O(1), dequeue : O(1)
'''

# (1) Python list로 구현한 stack
class Stack1:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        self.items == []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        if self.is_empty():
            return None
        else:
            self.items[len(self.items)-1]

    def pop(self):
        if self.is_empty():
            return None
        else:
            self.items.pop()

    def size(self):
        return len(self.items)

# stack linked list로 구현
class Node :
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack2:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def push(self,item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def pop(self):
        if self.is_empty():
            return None
        else :
            temp = self.head
            self.head = temp.next
            return temp.item

    def peek(self):
        if self.is_empty():
            return None
        else :
            return self.head.item

    def size(self):
        current = self.head
        count=0
        while current != None:
            count+=1
            current = current.next
        return count

# queue list로 구현
class Queue1:
    def __init__(self):
        self.items =[]
    def is_empty(self):
        return self.items==[]
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            return None
        else :
            return self.items.pop(0)
    def size(self):
        return len(self.items)

# queue circular linked list로 구현
class Queue2:
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

    def size(self):
        count = 0
        temp = self.head.next
        current = temp
        if self.is_empty():
            return count
        else :
            while True :
                count +=1
                current = current.next
                if current != temp:
                    continue
                else :
                    break
        return count