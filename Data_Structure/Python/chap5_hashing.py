'''
해야할 일 : 이차 조사 구현하기

1. hashing
: 데이터 키 값을 간단한 함수를 사용해 변환한 mapping한 값을 리스트의 인덱스로 사용하여 데이터를
  리스트에 저장하는 절차로 공간 낭비를 줄이면서 키 값을 이용한 데이터 검색의 시간 복잡도를 가능하다면 o(1)로 유지하기 위해 사용
- hash function(해쉬 함수) : 해싱에 사용되는 함수
- hash value(해쉬 값) or hash address(해시 주소): 해쉬 함수가 계산한 값
- hash table(해시 테이블) : 해시 데이터가 해시 값에 따라 저장된 구조
즉, hash function을 통해 큰 키 공간(key space/domain)을 작은 주소 공간(address space)으로 변환

- 적절한 조치를 취한 해싱은 데이터의 수 n이 증가하여도 검색 시간에 영향을 주지 안흠
- 이상적일 경우 키 값을 이용하여 데이터를 검색할 경우 시간 복잡도는 o(1)
- 해쉬값이 같을 경우, 충돌(collision)이 발생

(1) hash function
- division 함수 : 키 값을 소수(prime numver)로 나눈 뒤, 그 나머지 값을 해시 값으로 사용
- 중간 제곱 함수 : 키 값을 제곱한 후, 적절한 크기의 중간 부분을 해시 값으로 사용
- 이동 접기 : 키 값을 주소 공간의 자릿수와 동일하게(마지막 그룹은 아닐 수 있음) 여러 부분으로 분할하고 이들의 합을 이용해 해시값으로 사용
- 경계 접기 : 키 값을 주소 공간의 자릿수와 동일하게(마지막 그룹은 아닐 수 있음) 여러 부분으로 나누고 이들을 접고 그 합을 이용해 해시값으로 사용
- 곱셈 함수 : 키 값에 0.61803을 곱하여 얻은 소수부분에 해시 테이블 크기 m을 곱한 정수 부분을 해시값으로 사용
- 숫자 분석 혹은 숫자 추출 함수 : 키 값들의 모든 자릿수에 대한 빈도 테이블을 만들고, 균등한 분포를 갖는 자릿수의 조합을 해시 값으로 사용

1) 좋은 해시 함수의 조건
- 해시 값이 주소 공간 내에 균등하게 분포되어야 함
- 충돌 빈도가 잦지 않아야 함
- 계산이 빨라야 함

(2) hash table
- 각 버킷은 s개의 슬롯을 가질 수 있음 ex) list에서 7개의 버킷은 각각 1개의 슬롯을 가져서 총 7개의 슬롯을 가지게 됨
- 버킷이 가지는 슬롯 수보다 많이 충돌이 발생하면 버킷에 더 이상 데이터를 저장할 수 없게 되는 오버 플로우가 발생함
- list를 사용하면 충돌이 한번만 발생하도 바로 오버플로우가 발생하므로 충돌을 해결할 방법이 필요

2. 개방주소 & 폐쇄주소 방식
- 개방주소 방식 : 충돌이 발생하면 해시 테이블 내의 새로운 슬롯을 조사하여 충돌된 데이터를 삽입하는 방식으로
               선형 조사, 이차조사, 랜덤 조사, 이중 해싱 등이 이에 해당됨
               처음에 주어진 해시 테이블 공간 안에서 충돌을 해결하므로 폐쇄 해싱(closed hasing)
- 폐쇄주소 방식 : 충돌이 발생하더라도 키 값에 대한 해시값을 가지는 슬롯에만 데이터를 삽입하는 방식으로
               체이싱이 이에 해당됨
               처음에 주어진 해시 테이블의 공간 밖에 새로운 공간을 할당하여 충돌을 해결하므로 개방 해싱(open hashing)

3. 충돌 해결 방법
1) linear probing(선형 조사) 방법
- 삽입 연산 : 충돌이 일어난 슬롯에서부터 순차적으로 방문하여 처음 발견한 empty 슬롯에 데이터를 삽입
            충돌 시 순차적으로 빈 슬롯을 찾아 데이터를 저장하므로 해시 테이블 내의 데이터들이 빈틈없이 뭉쳐지는 clustering 현상 발생
- 검색 연산 : 슬롯[해시 값]부터 시작하여 1. 데이터를 찾거나 2. 빈 슬롯을 만나거나 3. 모든 슬롯을 전부 방문할 때까지
            순차적으로 해시값을 증가시켜 가면서 슬롯을 검사
- 삭제 연산 : 검색 연산과 동일하나, 2.의 빈 슬롯을 한번도 사용하지 않은 슬롯과 사용되었다가 데이터가 삭제되어 현재는 비어있는 슬롯으로 구분해야 함.

4. quadratic probing(이차 조사) 방법
: 삽입/검색/삭제 시 충돌이 일어난 슬록에서부터 (key+1)%m, (key+4)%m, (key+9)%m ,,, 순서로 삽입/삭제/삭제를 함
- 선형 조사의 군집화 현상의 문제점을 해결할 수 있지만, 서로 다른 키 값을 가지는 데이터가 같은 해시 값을 가지게 되는 경우,
  똑같은 점프 순서로 탐색하므로 또다른 형태의 군집화 현상인 2차 군집화 현상이 발생함
- 삽입 시 empty 슬롯이 존재하는데도 empty 슬롯을 건너뛰어 삽입에 실패하는 경우도 피할 수 없음
  즉, 해시 테이블이 꽉 찬 상태가 아니어도 empty 슬롯을 반드시 발견한다고 보장할 수 없음
- 해시 테이블의 적재율(loading factor) : 저장되는 데이터 수(n)과 해시테이블의 크기(m)의 비율 알파=n/m
  만약, 해시 테이블의 크기 m이 소수(prime number) & 알파 < 0.5인 경우, 이차 조사는 반드시 empty 슬롯을 찾을 수 있음
  알파>0.5인 경우, 삽입 검색 삭제를 위한 슬롯 방문수가 급격하게 증가함

5. chaining(체이닝)
: 해시 테이블의 각 소켓이 한 개 이상의 데이터를 저장할 수 있도록 충돌된 데이터들의 단순 연결 리스트를 저장
- 해시 테이블의 적재율(loading factor)인 알파에 큰 영향을 받지 않음
- 나눗셈 해시 함수와 체이닝을 사용할 경우 가장 좋은 성능을 보임

'''

class LinearProbing:
    def __init__(self, size):
        self.m = size
        self.k = [None for _ in range(size+1)] # 키 값 저장
        self.d = [None for _ in range(size+1)] # 데이터 값 저장

    def hash(self, key): # 키 값을 해쉬 값으로 변환
        return key % self.m

    def insert(self, key, data):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while True:
            if self.k[i] == None or self.k[i] == '$': # 빈 슬롯
                self.k[i] = key
                self.d[i] = data
                return None
            if self.k[i] == key: # 삽입하고자 하는 키 값이 존재한다면 데이터 값만 바꿈
                self.d[i] = data
                return None
            # 충돌 발생
            j += 1
            i = ( initial_position + j ) % self.m # 다음 while 루프에서 방문할 슬롯의 위치 결정
            if i == initial_position : # 빈 슬롯이 없으므로 삽입 실패
                break

    def search(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while self.k[i] != None:
            if self.k[i] == key:
                return self.d[i]
            j += 1
            i = (initial_position +j) % self.m
            if i == initial_position: # 검색 실패
                break
        return None

    def delete(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while self.k[i] != None:
            if self.k[i] == key:
                self.k[i] = '$'
                self.d[i] = None
                return None
            j += 1
            i =(initial_position +j) % self.m
            if i == initial_position:
                break
        return None

    def print_table(self):
        for i in range(self.m) : print("%-6d" %i , end ='')
        print()
        for i in range(self.m):
            if type(self.k[i]) == int : print("%-6d" %self.k[i], end='')
            elif self.k[i] == "$" : print("$     ", end='')
            else : print(self.k[i], end='  ')
        print()
        for i in range(self.m):
            if type(self.d[i]) == str : print(self.d[i], end='     ')
            else : print(self.d[i], end='  ')

class Node :
    def __init__(self, key, data, link):
        self.key = key      # key field : 데이터의 키 값을 저장
        self.data = data    # data field : 데이터 값을 저장
        self.next = link    # link field : 다음 순서 노드의 참조를 저장( 데이터를 노드로 저장 )

class Chaining :
    def __init__(self, size):
        self.m = size
        self.table = [None for x in range(size+1)]
        # 해시 테이블의 각 항목 table[i]는 해시 값 i를 가지는 데이터들을 저장하는 노드들의 연결리스트의 첫 노드를 가리키는 head 역할을 함

    def hash(self, key):
        return key % self.m

    def insert(self, key, data):
        i = self.hash(key)
        p = self.table[i]
        while p != None :
            if key == p.key:
                p.data = data
                return None
            p = p.next
        self.table[i] = Node(key, data, self.table[i]) # link list 맨 앞에 삽입 o(1)

    def search(self, key):
        i = self.hash(key)
        p = self.table[i]
        while p != None:
            if key == p.key:
                return p.data
            p = p.next
        return None

    def delete(self, key):
        i = self.hash(key)
        p = self.table[i]
        previous = None
        while p != None:
            if key == p.key:
                if previous == None: # 첫 노드가 delete할 값인 경우
                    self.table[i] = p.next
                else :
                    previous.next = p.next
                return None
            previous = p
            p = p.next

    def print_table(self):
        for i in range(self.m):
            print("%2d" %i, end='')
            if self.table[i] != None:
                p = self.table[i]
                while p != None:
                    print(" --> [", p.key, ",", p.data,"]", end='')
                    p = p.next
            print()

if __name__ == '__main__':
    # ht = LinearProbing(13)
    # ht.insert(45,'A')
    # ht.insert(27,'B')
    # ht.insert(88,'C')
    # ht.insert(9,'D')
    # ht.insert(71,'E')
    # ht.insert(60,'F')
    # ht.insert(46,'G')
    # ht.insert(38,'H')
    # ht.insert(24,'I')
    #
    # print("######### 선형 조사 방법 ########")
    # print("해시 테이블 : ")
    # ht.print_table()
    # print()
    # print("\nkey 값이 46인 data 검색 결과 : ", ht.search(46))
    # ht.delete(60)
    # ht.delete(46)
    # print("\nkey 값이 60인 F 삭제 후, key 값이 46인 G를 삭제한 해시 테이블 : ")
    # ht.print_table()

    ht = Chaining(13)
    ht.insert(45, 'A')
    ht.insert(27, 'B')
    ht.insert(88, 'C')
    ht.insert(9, 'D')
    ht.insert(71, 'E')
    ht.insert(60, 'F')
    ht.insert(46, 'G')
    ht.insert(38, 'H')
    ht.insert(24, 'I')

    print("######### 체이싱 방법 ##########")
    print("해시 테이블 : ")
    ht.print_table()
    print()
    print("key 값이 9인 data 검색 결과 : ", ht.search(9))
    ht.delete(71)
    ht.delete(45)
    print("\nkey 값이 71인 E 삭제 후, key 값이 45인 A를 삭제한 해시 테이블 : ")
    ht.print_table()