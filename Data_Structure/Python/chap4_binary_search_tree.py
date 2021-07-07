'''
- 차수가 k인 트리에 존재하는 노드의 수가 n일 때, none값을 저장하고 있는 링크 필드 수 = n*k - (n-1)

1. binary tree : 왼쪽자식, 오른쪽 남매로 표현 = k를 2로 제한
- 자식노드의 순서를 구별함( tree는 하지 않음 )
- empty인 트리가 존재( tree는 1개 이상 )
- 레벨 i에 존재할 수 있는 최대 노드의 수 = 2^i
- T[i] 노드의 왼쪽 자식 노드 = T[2*i+1], 오른쪽 자식 노드 = T[2*(i+1)], 부모 노드 = T[(i-1)//2] 단 i>0

1) 완벽 이진 트리 : 각 내부 노드 모두가 두개의 자식노드를 가진 트리
- 모든 노드의 수 : 2^(h+1)-1    h = 높이
- 높이 h = log2(n+1)-1

2. binary search tree
- 모든 노드들의 키는 서로 다른 유일한 값을 가짐
- 특정 노드 n의 키 값이 n의 왼쪽 서브 트리에 존재하는 모든 노드들의 키 값보다 크고, n의 오른쪽 서브 트리에 있는 모든 노드들의 키 값보다 작음
- 중위순회 시 정렬된 값이 나옴( LNR )
- n의 왼쪽 서브 트리와 오른쪽 서브 트리도 이진 탐색 트리임 ( 재귀적 )

'''
from chap3 import Queue2

class Node:
    def __init__(self, item, left_child=None, right_child = None):
        self.key = item
        self.left = left_child
        self.right = right_child

class BinaryTree :
    def __init__(self): #O(1)
        self.root = None
    # 깊이 우선
    def preorder(self, node): #O(n) 전위순회 NLR
        print(node.key, " ", end='')
        if node.left :
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)

    def inorder(self, node): #O(n) 중위순회 LNR
        if node.left :
            self.inorder(node.left)
        print(node.key, " ", end='')
        if node.right:
            self.inorder(node.right)

    def postorder(self, node): #O(n) 후위순회 LRN
        if node.left :
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        print(node.key, " ", end='')

    # 너비 우선 : 좌에서 우로
    def levelorder(self, node): #O(n)
        q = Queue2()
        q.enqueue(node)
        while not q.is_empty():
            node = q.dequeue()
            print(node.key, " ", end='')
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)


class BST : # o(h) 이때 h=트리의 높이. 즉, o(log n) but, 편향된 이진탐색 트리면 o(n)
    def __init__(self):
        self.root = None

    def search(self, k):
        return self._search(self.root, k)
    def _search(self, n, k):
        if n == None or n.key == k:
            return n != None
        elif n.key > k:
            return self._search(n.left, k)
        else :
            return self._search(n.right, k)

    def insert(self, key):
        self.root = self._insert(self.root, key)
    def _insert(self, n, key):
        if n == None:
            return Node(key)
        if n.key > key:
            n.left = self._insert(n.left,key)
        elif n.key < key: # else면 중복된 키값도 가지는 트리가 되므로 안됨
            n.right = self._insert(n.right,key)
        return n # tree가 이어질 수 있도록 꼭 써야함

    def find_min(self):
        if self.root == None:
            return None
        return self._find_min(self.root)
    def _find_min(self, n):
        if n.left == None:
            return n.key
        return self._find_min(n.left)

    def _find_max(self, n):
        if n.right == None :
            return n.key
        return self._find_max(n.right)

    def delete_min(self):
        if self.root == None:
            print("Tree is empty")
        self.root = self._delete_min(self.root)
    def _delete_min(self,n):
        if n.left == None:
            return n.right
        n.left = self._delete_min(n.left)
        return n

    def _delete_max(self,n):
        if n.right == None:
            return n.left
        n.right = self._delete_max(n.right)
        return n

    # 중위 후속자 사용
    def delete(self, key):
        self.root = self._delete(self.root, key)
    def _delete(self, n, key):
        if n == None:
            return None
        if n.key > key:
            n.left = self._delete(n.left,key)
        elif n.key < key:
            n.right = self._delete(n.right,key)
        else:
            if n.left == None and n.right == None: # case 1 : n의 자식노드가 없는 경우
                return None
            if n.left == None or n.right == None: # case 2 : n의 자식노드가 1개 있는 경우
                if n.left == None:
                    return n.right
                else:
                    return n.left
            target = n # case 3
            n = self._find_min(target.left) # n의 중위 후속자 : n의 오른쪽 서브 트리에서 가장 작은 값
            n.right = self._delete_min(target.left)
            n.left = target.left
        return n

    # 중위 선행자 사용
    def delete2(self, key):
        self.root = self._delete(self.root, key)
    def _delete2(self, n, key):
        if n == None:
            return None
        if n.key > key:
            n.left = self._delete(n.left,key)
        elif n.key < key:
            n.right = self._delete(n.right,key)
        else:
            if n.left == None and n.right == None: # case 1 : n의 자식노드가 없는 경우
                return None
            if n.left == None or n.right == None: # case 2 : n의 자식노드가 1개 있는 경우
                if n.left == None:
                    return n.right
                else:
                    return n.left
            target = n # case 3
            n = self._find_max(target.right) # n의 중위선행자 : n의 왼쪽 트리 중 가장 큰값
            n.left = self._delete_max(target.right)
            n.right = target.right
        return n

    def inorder(self, node): #O(n) 중위순회 LNR
        if node.left :
            self.inorder(node.left)
        print(node.key, " ", end='')
        if node.right:
            self.inorder(node.right)

if __name__ == '__main__':
    t = BST()
    t.insert(10)
    t.insert(20)
    t.insert(50)
    t.insert(60)
    t.insert(80)
    t.insert(90)
    t.insert(30)
    t.insert(40)
    print("inorder : ", end='')
    t.inorder(t.root)
    print("\n20이 tree에 있는가? :", t.search(20))
    print("tree에서 가장 작은 값 : ", t.find_min())
    t.delete_min()
    print("delete min 후 inorder : ", end='')
    t.inorder(t.root)
    t.delete(60)
    print("\n60 delete 후 inorder : ", end='')
    t.inorder(t.root)
    t.delete2(80)
    print("\n80 delete2 후 inorder : ", end='')
    t.inorder(t.root)