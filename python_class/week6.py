def calcsum(n):
    sum=0
    for num in range(n+1):
        sum+=num
    return sum
print("~4 = ", calcsum(4))
print("~10 = ", calcsum(10))

def calcrange(begin, end):
    sum=0
    for num in range(begin, end+1):
        sum+=num
    return sum
print("3~7 = ", calcrange(3,7))

def printsum(n):
    sum=0
    for num in range(n+1):
        sum+=num
    print("~",n,"=",sum)
printsum(4)
printsum(10)

def intsum(*ints):
    sum=0
    for num in ints:
        sum+=num
    return sum
print(intsum(1,2,3))
print(intsum(5,7,9,11,13))
print(intsum(8,9,6,2,9,7,5,8))

def calcstep(begin, end, step):
    sum=0
    for num in range(begin, end+1, step):
        sum+=num
    return sum
print("1~10 = ", calcstep(1,10,2))
print("2~10 = ", calcstep(2,10,2))

def calcstep(begin, end, step=1):
    sum=0
    for num in range(begin, end+1, step):
        sum+=num
    return sum
print("1~10 = ",calcstep(1,10,2))
print("1~100 = ", calcstep(1,100))

print("3~5 = ", calcstep(3,5,1))
print("3~5 = ", calcstep(begin=3, end=5, step=1))
print("3~5 = ", calcstep(step=1, end=5, begin=3))
print("3~5 = ", calcstep(3,5, step=1))
print("3~5 = ", calcstep(3, step=1, end=5))

coffee = int(input("어떤 커피 드릴까요? (1:보통, 2: 설탕, 3: 블랙)"))
print()
print("# 1. 뜨거운 물을 준비한다 #")
print("# 2. 종이컵을 준비한다 #")

if coffee == 1 :
    print("# 3. 보통 커피를 탄다 #")
elif coffee==2:
    print("# 3. 설탕 커피를 탄다 #")
elif coffee==3:
    print("# 3. 블랙 커피를 탄다 #")
print("# 4. 물을 붓는다 #")
print("# 스푼으로 저어서 녹인다 #")