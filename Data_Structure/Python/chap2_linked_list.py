'''
단순연결리스트 구성하는 단위 = 노드 : 데이터 필드 + 링크 필드로 구성

(1) 단순 연결 리스트 vs list
- index를 통한 검색 : O(n) vs O(1)
- item을 통한 검색 : O(n) vs O(n)
- 단 정렬된 list의 검색 성능은 항상 단순연결 리스트보다 좋음 why? 이진탐색 O(logn)
- 처음 위치에 삽입 : O(1) vs O(n)
- 어떤 index에 삽입 : O(n) vs O(n)
- 마지막 index에 삽입 : O(n) vs O(1)
- 첫 항목 삭제 : O(1) vs O(n)
- item을 통한 삭제 : O(n) (O(n)+O(1)) vs O(n) (O(n)+O(n))

(2) 정렬된 단순 연결 리스트
- 검색 : O(n)
'''

class Node :
    def __init__(self, item):
        self.item = item
        self.next = None
    def get_item(self):
        return self.item
    def get_next(self):
        return self.next
    def set_item(self, new_item):
        self.item = new_item
    def set_next(self, new_next):
        self.next = new_next

# Singly linked list
class Slist :
    def __init__(self): #O(1)
        self.head = None

    def is_empty(self): #O(1)
        return self.head==None

    def add(self, item): #O(1)
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self): #O(n)
        count = 0
        current = self.head
        while current != None:
            count+=1
            current = current.next
        return count

    def search(self, item): #O(n)
        current = self.head
        found = False
        while current != None and not found :
            if current.item == item :
                found = True
            else:
                current = current.next
        return found

    def delete(self, item): #O(n) # item이 반드시 존재한다고 가정
        current = self.head
        previous = None
        found = False
        while not found:
            if current.item == item :
                found = True
            else :
                previous = current
                current = current.next
        if previous == None :
           self.head = current.next
        else:
           previous.next = current.next

    def append(self, item):
        temp = Node(item)
        if self.is_empty():
            self.head = temp
        else :
            current = self.head
            while current.next != None :
                current = current.next
            current.next = temp

    def pop_first(self):
        self.head = self.head.next

    def pop_last(self):
        current = self.head
        previous = None
        while current.next != None:
            previous = current
            current = current.next
        previous.next = None

# Ordered Singly Linked List
class OList:
    def __init__(self):
        self.head = None

    def add(self,item): #O(n)
        current = self.head
        previous = None
        stop = False
        while current != None and not stop :
            if current.item > item :
                stop = True
            else :
                previous = current
                current = current.next
        temp = Node(item)
        if previous == None :
            temp.next = self.head
            self.head = temp
        else :
            temp.next = current
            previous.next = temp

    def search(self, item ): # O(n)
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop :
            if current.item == item :
                found = True
            else :
                if current.item > item :
                    stop = True
                else :
                    current = current.next
            return found

class CList :
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        if self.is_empty():
            temp.next = temp
            self.head = temp
        else :
            temp.next = self.head.next
            self.head.next = temp

    def append(self, item):
        temp = Node(item)
        if self.is_empty():
            temp.next = temp
            self.head = temp
        else:
            temp.next = self.head.next
            self.head.next = temp
            self.head = temp

    def pop_first(self):
        if self.head == None:
            print("empty")
        else :
            temp = self.head.next
            if temp == temp.next():
                self.head = None
            else :
                self.head.next = temp.next

    def search(self, item):
        if self.head == None :
            print("empty")
        else:
            temp = self.head.next
            if self.head == temp:
                if temp.item == item :
                    return True
                else:
                    return False
            found = False
            current = temp
            while True :
                if current.item == item :
                    found = True
                else:
                    current = current.next
                if current != temp and not found :
                    continue
                else:
                    break
        return found

if __name__ == '__main__':
    s = Slist()
    s.add(10)
    s.add(20)
    s.add(30)
    answer = s.search(20)
    print(answer)
    s.append(40)