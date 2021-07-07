'''
(1) 학생 데이터를 학번과 관계없이 무작위로 나열
- 검색 : 선형탐색(linear search) 알고리즘  O(N)

(2) 학생 데이터를 오름차순/내림차순으로 나열
- 검색 : 이진탐색(binary search) 알고리즘  O(logN)
- (1)비해 항상 시간적으로 효율적이진 않음, 만약 학생 데이터가 자주 삽입/삭제 된다면 학생 데이터 관리에 많은 시간을 낭비하게 됨

(3) 이진탐색트리(BST : Binary Search Tree) 형태로 나열
- 균형잡힌 트리라면, 검색/삽입/삭제 연산도 빠르게 할 수 있음 O(logN)
- (2)비해 항상 시간적으로 효율적이진 않음, 만약 편향된 BST 형태라면 (2)보다 느림


자료구조 학습 필요성
: 특정 문제 해결에 적합한 논리적 구조를 선택할 수 있는 능력을 키울 수 있으며,
 선형구조인 컴퓨터(메모리)에 다양한 논리적 구조를 가진 데이터들이 저장될 수 있는지 이해할 수 있음
- 선형 구조 : 데이터 간의 앞뒤 관계가 일대일
  ex) list(논리적 구조 = 물리적 구조), linked list(논리적 구조 != 물리적 구조), stack, queue
- 비선형 구조 : 데이터 간의 앞뒤 관계가 일대일로 고정되어있지 않은 구조 ex) tree, graph


자료(데이터) 추상화
- 현실 세계의 특정 유/무형 개체를 데이터로 표현하기 위해 해당 개체의 공통적이고 핵심적인 특징만을 간추려 내는 것
- 즉, 데이터들의 논리적 구조 및 관련 연산을 구체적으로 어떻게 프로그램으로 구현해야 한다는 세부 사항을 숨기는 것
- 자료 구조 : 특정 문제 해결에 대한 ADT의 연산이 가장 효율적으로 수행될 수 있도록 데이터들에 대한 논리적 구조를 설계하고 저장한 것


- 알고리즘의 시간 복잡도 분석 : 입력 크기에 따라서 기본연산이 몇번 수행되는지 결정하는 절차
- 4가지의 시간 복잡도 분석 방법 : 최악, 최선, 평균, 모든
(1) 최악의 경우 분석 : W(n) 입력(입력크기 + 입력값)에 대해 기본 연산 수행 횟수가 최대인 경우
(2) 최선의 경우 분석 : B(n) 입력(입력크기 + 입력값)에 대해 기본 연산 수행 횟수가 최소인 경우
(3) 평균의 경우 분석 : A(n) 입력(입력크기 + 입력값)에 대해 입력 값의 확률분포를 가정 후,모든 입력값에 대해 기본 연산이 수행되는 횟수의 평균
(4) 모든 경우의 분석 : T(n) 입력값의 내용과 무관하게 복잡도가 항상 일정한 경우에만 가능 = 시간복잡도는 입력 크기에만 종속적임
                    ex) sum(dataset) : for i in dataset : result += i : 리스트 안에 있는 값과 상관없이 기본연산만 수행
                    즉, 모든 경우의 분석이 가능하다면 W(n) = B(n) = A(n)임
- 선택한 기본 연산에 대해서 최악/최선/평균의 시간 복잡도가 동일한 경우 모든 경우의 분석 사용
- 다른 경우 최악/평균 경우 분석을 사용

- 알고리즘의 점근적 복잡도 : 입력 크기 n의 값이 무한히 큰 경우일때의 시간 복잡도
- 이 각각의 시간 복잡도 분석 방법은 아래의 점근 표기법으로 표기할 수 있음
- 점근표기법 : O(big-Oh), big-Omega, Theta

(1) O(big-Oh) 표기법
: 모든 n>n0에 대해서 f(n) <= c*g(n)이 성립하는 임의의 양의 상수 c, n0가 존재하면, f(n)=O(g(n))임
- 즉 g(n)을 f(n)의 상한(upper bound)이라고 함
- 더 큰 차수 가능

(2) Omega 표기법
: 모든 n>n0에 대해서 f(n) >= c*g(n)이 성립하는 양의 상수 c, n0가 존재하면, f(n)=omega(g(n))
- 즉 g(n)을 f(n)의 하한(lpper bound) 이라고 함
- 더 작은 차수 가능

(3) Theta 표기법
: 모든 n>n0에 대해서 c1*g(n) >= f(n) >= c2*g(n)이 성립하는 양의 상수 c1, c2, n0이 존재하면 f(n)=Theta(g(n))
- O 표기와 Omega 표기가 동일한 경우에 사용


python의 내장 데이터 타입
- 스칼라 데이터 타입 : int, float, None(하나의 인스턴스), boolean
- 컬렉션 데이터 타입 : 순서열 데이터 타입( str, list, tuple), 매핑 데이터 타입(dict), 집합 데이터 타입(set)
- 사용자 정의 데이터 타입 : 데이터 = 속성(객체를 기술하는 특성) = memeber 변수, 연산 = 기능 = member 함수/메소드
- 수정 가능한 컬렉션 데이터 타입 : list, dict, set       수정 불가능 : str, tuple


- 객체(object) : python에서 모든 데이터는 객체임( 함수, 클래스도 객체 )
- 클래스 : 사용자 정의 데이터 타입의 객체를 만들기 위한 도구
- 객체는 클래스에 의해 생성되며 특정 클래스 C에 의해 생성되는 객체 O를 C의 인스턴스라고 함
  ex) 23 : int class의 인스턴스이자 정수 객체


- 재귀 호출 함수 : 기본 케이스( 종료 시점 ), 재귀 케이스
'''

#(1)
import random
import time
random.seed(time.time())
a = list()
for _ in range(1000):
    a.append(random.randint(1,1000))
start_time = time.time()
a.sort(reverse = True)
print(time.time()-start_time, "seconds")

#(2) linear search
def linear_search(target, dataset):
    for i in range(len(dataset)):
        if dataset[i] == target:
            return i
    return "NOT found"

dataset = [15,20,30,50,3,40]
result = linear_search(40, dataset)

#(3) 구구단 프로그램
for i in range(1,10):
    for j in range(1,10):
        print(i ,"x", j , "=", i*j, end = ' ')
    print()

# student class
class Student :
    univ = "SKKU" # 클래스 변수 : class의 모든 객체가 공유하는 속성을 위한 변수
    def __init__(self, name, id): # 생성자
        self.name = name # 멤버변수 : 각각의 객체의 속성을 위한 변수
        self.id = id     # 멤버 변수
    def get_name(self):  # 멤버 함수(메소드)
        return self.name
    def get_id(self):    # 멤버 함수(메소드)
        return self.id

#(4) list 이용
assistant = []
num_ass = int(input("input the number of assistant : "))
for i in range(num_ass):
    new_name = input("please enter a name : ")
    new_id = input("please enter a id : ")
    assistant.append(Student(new_name, new_id))
for j in range(num_ass):
    print(j, assistant[j].get_name(), assistant[j].get_id())

#(5) stack 이용
class Stack:
    def __init__(self):
        self.items=[]
    def push(self, item):
        self.items.append(item)
    def peek(self):
        return self.items[len(self.items)-1]
    def pop(self):
        self.items.pop()

assistant = Stack()
num_ass = int(input("input the number of assistant : "))
for i in range(num_ass):
    new_name = input("please enter a name : ")
    new_id = input("please enter a id : ")
    assistant.push(Student(new_name,new_id))
for j in range(num_ass):
    print(j, assistant.peek().name, assistant.peek().id)
    assistant.pop()

#(6) factorial
def factorial(n): # O(n)
    if n==1 :
        return 1
    else:
        return n * factorial(n-1)

#(7) fibo
def fibo(n): #O(2^n)
    if n<=2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

#(8) binary search
def binary_search(dataset, left, right, target):
    if left > right :
        return "Not found"
    else :
        mid = (left+right)//2
        if dataset[mid] == target :
            return mid
        elif dataset[mid] > target :
            binary_search(dataset, left, mid-1, target)
        else:
            binary_search(dataset, mid+1, right, target)
