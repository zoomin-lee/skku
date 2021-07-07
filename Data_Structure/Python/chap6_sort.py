'''
(1)정렬이란? 정렬 키를 기준으로 오름차순 혹은 내림차순으로 재배열시키는 연산
- 정렬은 탐색 성능을 향상시키기 위해서도 필수적임

(2)내부 정렬 : 정렬할 항목들의 집합 D가 주기억장치(메인 메모리)에 상주할 수 있는 경우, D를 주기억장치에서 정렬

(3)선택 정렬 o(n^2)
1. n개의 항목으로 이루어진 python 리스트 item에서 가장 작은 원소를 찾음
2. 가장 작은 원소가 item[j]라면 item[i](i=0)의 위치를 서로 교환
3. i+=1한 후, items[0]을 제외한 나머지 원소에 대해서 가장 작은 원소를 찾은 후, 교환을 반복
- 원소 비교 횟수 : n(n-1)/2 = o(n^2)
- 입력에 민감하지 않음 : 어떠한 입력에 대해서도 항상 o(n^2)의 수행 시간이 소요됨
- 값이 최소인 원소를 찾은 후 원소의 위치를 교환하는 최대횟수가 n-1번으로
  정렬 알고리즘들 중에서 (최악의 경우) 가장 적은 위치 교환 횟수임

(4) 삽입 정렬 o(n^2)
1. items 내 n개의 원소 정렬 시 첫 원소 item[0]은 이미 정렬되었다고 취급
2. 다음 원소 items[1]을 정렬된 부분 item[0]과 비교하여 적절한 위치에 삽입,,,, 반복
- 입력이 역으로 정렬되어 있는 최악의 경우 : 원소 비교 횟수( n(n-1)/2 = o(n^2) ) + 원소 교환 횟수( n(n-1)/2 = o(n^2) )
- 입력에 민감함 : 입력의 정렬 순서에 따라 소요되는 수행이 변함 ( 정렬 : n-1번의 비교 = o(n) )
- 이미 정렬된 데이터의 뒷부분에 소량의 신규 데이터를 추가하여 정렬하는 경우 즉, 입력이 거의 정렬된 경우 우수한 성능을 보임
입력의 사이즈가 작은 경우 우수한 성능을 보임

(5) 버블 정렬 o(n^2)

(6) 셸 정렬
: 일정한 간격 h로 떨어져 있는 원소들끼리 논리적인 서브리스트를 구성하고 각 서브리스트에 있는 원소들에 대해서
  삽입정렬을 수행하는 연산을 반복하면서 전체 원소들을 정렬하는 알고리즘
- h 정렬 : 간격이 h인 원소들로 구성된 h개의 서브리스트에 대해 삽입 정렬을 수행하는 알고리즘
          삽입 정렬을 수행하기 전에 작은 값은 리스트 앞부분으로 큰 값은 뒷부분으로 옮기는 전처리 과정임
          h=1인 경우 삽입 정렬과 동일 but 이미 부분적으로 정렬된 원소들의 수가 많아져서 속도가 빠름
- 즉, 셸 정렬은 삽입 정렬은 입력이 거의 정렬된 경우 및 입력의 사이즈가 적은 경우 좋은 성능을 보인다는 사실에 의해 고안된 알고리즘
- 이때, 간격 h는 n//2, n//4, n//8, n//16 ,,, 1로 수행
- h에 따라 수행시간이 달라지므로 정확한 분석은 어려움
- 일반적으로 입력의 사이즈가 작을 때 성능이 좋음

(7) 힙 정렬 o(n log n)
1. list를 max 힙으로 구성
2. 루트 노드를 힙의 가장 마지막 교환한 후, 힙 사이즈(list의 사이즈)를 1 감소시키고
   노드 교환으로 인해 위배한 힙 속성을 downheap연산으로 복원하는 과정을 힙사이즈가 1이 될떄까지 반복
- 상향식(bottom-up)으로 힙을 구성하는 시간  : o(n)
  루트 노드와 힙의 마지막 노드를 교환한 후 downheap 수행 시간 : o(log n)
  루트 노드와 힙의 마지막 노드를 교환하는 횟수 : n-1
  따라서, o(n) + (n-1)*o(log n) = o(n log n)
- 입력에 민감하지 않음
- 일반적으로 입력의 사이즈가 큰 경우 성능이 좋지 않음

(8) 합병 정렬 o(n log n)
1. list 내 n개의 원소 정렬 시 low, mid, high를 찾은 후, 두 서브 리스트로 분할
2. 모든 서브리스트의 사이즈가 1이 될 때까지 재귀적으로 분할 (분할 정복 알고리즘)
3. 분할 과정이 끝나면, n개의 원소를 포함하는 하나의 리스트가 생성될 때까지 각각의 서브 리스트를 결합 및 정렬
- 입력에 민감하지 않음
- 정렬 시 추가 메모리 공간이 필요함
- 자바 객체 정렬에서 시스템 sort로 활용

(9) 퀵 정렬 o(n log n)
1. 리스트 내 n개의 원소 정렬 시 피벗을 선택 ( 일반적으로 리스트의 첫번째 원소 )
2. 피벗을 기준으로 피벗보다 작은 원소들을 피벗의 왼쪽으로 옮기고, 피벗보다 큰 요소들은 모두 피벗의 오른쪽으로 옮겨서 두개의 서브 리스트를 생성
3. 피벗을 제외한 왼쪽 서브리스트와 오른쪽 서브리스트에 대해서도 서브 리스트의 사이즈가 0이나 1이 될 때까지 재귀적으로 분할
   ( 합병 정렬과 다르게 퀵 정렬은 분할 시 정렬)
4. 정렬된 서브리스트를 하나의 리스트로 자연스럽게 합병
- 입력크기 N=2^k라 가정
  최선의 경우 & 평균의 경우 o(n log n) : 합병 정렬과 마찬가지로 k(log n)만큼 분할하며, 각 분할마다 약 n번의 원소를 비교해야 하므로
  최악의 경우 o(n^2) : 이미 정렬되어 있거나 역순으로 정렬되어 있다면 n번 분할해야 하며, 각 분할마다 n번의 원소를 비교해야 하므로
- 평균 시간 복잡도가 o(n log n)인 다른 정렬 알고리즘들보다 빠름
- c언어 라이브러리의 qsort뿐만 아니라 unix, g++, visual C++ 등에서도 퀵정렬을 시스템 sort로 사용
'''

def selection_sort(items):
    for i in range(0,len(items)-1):
        minimum = i
        for j in range(i, len(items)):
            if items[minimum] > items[j]:
                minimum=j
        items[i], items[minimum] = items[minimum], items[i]

items = [40,10,70,30]
print("\n선택 정렬 전 : ", items)
selection_sort(items)
print("선택 정렬 후 : ", items)

def insertion_sort(items):
    for i in range(1, len(items)):
        for j in range(i, 0, -1):
            if items[j-1] > items[j]:
                items[j], items[j-1] = items[j-1], items[j]
            else :
                break

items = [40,10,20,50,70,30,90]
print("\n삽입 정렬 전 : ", items)
insertion_sort(items)
print("삽입 정렬 후 : ", items)

def bubble_sort(items):
    n = len(items)-1
    for i in range(n, 0, -1):
        for j in range(0, i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]

items = [40,10,20,50,70,30,90]
print("\n버블 정렬 전 : ", items)
bubble_sort(items)
print("버블 정렬 후 : ", items)

def shell_sort(items):
    h = len(items) // 2
    while h >= 1:
        for i in range(h, len(items)):
            j = i
            while j >=h and items[j] < items[j-h]:
                items[j], items[j - h] = items[j - h], items[j]
                j -=h
        print(h, "- 정렬 결과 : ", items)
        h //= 2

items = [40,10,20,50,70,30,90]
print("\n셸 정렬 전 : ", items)
shell_sort(items)
print("셸 정렬 후 : ", items)

def downheap(i, size):
    while 2 * i + 1 <= size:
        k = 2 * i +1
        if k < size -1 and items[k] < items[k+1]:
            k += 1
        if items[i] >= items[k]:
            break
        items[i] ,items[k] = items[k], items[i]
        i = k

def heapify(items):
    hsize = len(items)
    for i in range(hsize//2 - 1, -1, -1):
        downheap(i, hsize)

def heap_sort(items):
    N = len(items)
    for i in range(N):
        items[0], items[N-1] = items[N-1], items[0]
        downheap(0, N-2)
        N-=1

items = [40,10,20,50,70,30,90]
print("\n힙 정렬 전 : ", items)
heapify(items)
print("Max heap만들기 : ", items)
heap_sort(items)
print("힙 정렬 후 : ", items)


def merge(items, temp, low, mid, high):
    i = low
    j = mid+1
    for k in range(low, high+1):
        if i > mid:
            temp[k] = items[j]
            j +=1
        elif j > high:
            temp[k] = items[i]
            i +=1
        elif items[j] < items[i]:
            temp[k] = items[j]
            j +=1
        else :
            temp[k] = items[i]
            i +=1
    for k in range(low, high+1):
        items[k] = temp[k]

def merge_sort(items, temp, low, high):
    if high <= low:
        return None
    mid = low + (high-low)//2
    merge_sort(items, temp, low, mid)
    merge_sort(items, temp, mid+1, high)
    merge(items, temp, low, mid, high)

items = [40,10,20,50,70,30,90]
temp =[None]*len(items)
print("\n합병 정렬 전 : ", items)
merge_sort(items, temp, 0, len(items)-1)
print("합병 정렬 후 : ", items)

def partition(items, pivot, high):
    i = pivot +1
    j = high
    while True:
        while i < high and items[i] < items[pivot]:
            i += 1
        while j > pivot and items[j] > items[pivot]:
            j -= 1
        if j <= i:
            break
        items[i], items[j] = items[j], items[i]
        i += 1
        j -= 1
    items[pivot], items[j] = items[j], items[pivot]
    return j

def quick_sort(items, low, high):
    if low<high:
        pivot = partition(items, low, high)
        quick_sort(items, low, pivot-1)
        quick_sort(items, pivot+1, high)

items = [40,10,20,50,70,30,90]
print("\n퀵 정렬 전 : ", items)
quick_sort(items, 0, len(items)-1)
print("퀵 정렬 후 : ", items)