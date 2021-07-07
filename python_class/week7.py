def intsum(*ints):
    sum=0
    for num in ints:
        sum+=num
    return sum
print(intsum(1,2,3))
print(intsum(5,7,9,11,13))
print(intsum(8,9,6,2,9,7,5,8))

def calcstep(begin, end, step=1):
    sum=0
    for num in range(begin, end+1, step):
        sum+=num
    return sum
print("1~10 = ",calcstep(1,10,2))
print("1~100 = ", calcstep(1,100))

print("3~5 = ", calcstep(3,5,1))#위치 인수
print("3~5 = ", calcstep(begin=3, end=5, step=1))#키워드 인수
print("3~5 = ", calcstep(step=1, end=5, begin=3))
print("3~5 = ", calcstep(3,5, step=1))
print("3~5 = ", calcstep(3, step=1, end=5))
#앞쪽에 키워드 인수가 있으면 뒤쪽에 위치 인수가 올 수 없음

def calcstep(**args):
    begin=args['begin']
    end=args['end']
    step = args['step']
    sum=0
    for num in range(begin, end+1, step):
        sum+=num
    return sum
print("3 ~ 5 = ", calcstep(begin=3, end=5, step=1))
print("3 ~ 5 = ", calcstep(step=1, begin=3, end=5))

def calcscore(name, *score, **option):
    print(name)
    sum=0
    for s in score :
        sum+=s
    print("총점 : ", sum)
    if (option['avg']==True):
        print("평균 : ", sum/len(score))

calcscore("성균관대학교", 88, 98, 77 , avg=True)
calcscore("컴사응", 99,98,96,93, avg=False)

def kim():
    temp = "김과장의 함수" #지역변수
    print(temp)

kim()
# print(temp)

def lee():
    temp =2**10
    print(temp)
    return temp

def park(a):
    temp=a*2
    print(temp)

kim()
print(kim())
lee()
print(lee())
park(3)

salerate = 0.9 #전역변수
# print(temp)
def kim():
    print("오늘의 할인율 : ", salerate)
def lee():
    price = 1000
    print("가격 : ", price*salerate)
kim()
salerate=1.1
lee()

price=1000
def sale():
    price=500
    print(price)
sale()
print(price)

def calcsum(n):
    """1~n까지의 합계를 구해 리턴한다"""
    sum=0
    for i in range(n+1):
        sum+=1
    return sum
help(calcsum)

def dic_func(**para):
    for k in para.keys():
        print("%s --> %d 명입니다 " %(k, para[k]))
dic_func(아이오아이=11, 소녀시대=8, 걸스데이=4, A0A=7)

def func1():
    result =100
    return result

def func2():
    print("반환값 없는 함수 실행")

hap=0
hap=func1()
print("func1()에서 돌려준 값 --> %d" %hap)
func2()

def para2_func(v1, v2):
    result=0
    result=v1+v2
    return result

def para3_func(v1, v2, v3):
    result =0
    result = v1+v2+v3
    return result

hap=0
hap=para2_func(10,20)
print("매개변수 2개 함수 호출 결과 --> %d" %hap)