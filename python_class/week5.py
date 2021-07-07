student=1
while student <= 5:
    print(student, "번 학생의 성적을 처리한다.")
    student +=1

num=1
sum=0
while num<= 100:
    sum+=num
    num+=1
print("sum = ", sum)
print(num)

for student in [1,2,3,4,5]:
    print(student, "번 학생의 성적을 처리한다.")

sum=0
for num in range(1 , 101):
    sum +=num
print("sum = ", sum)

for i in range(0,3,1):
    print("%d :for 문을 공부중입니다" %i)

for i in range(2,-1,-1):
    print("%d : for문을 공부중입니다" %i)

for i in range(1,6,1):
    print(i, end=" ")

for i in range(1, 6, 1):
    print("%d" %i, end=" ")

print("\n")

i, hap=0, 0
for i in range(1,11,1):
    hap=hap+i
print("1에서 10까지의 합 : " , hap)

i, hap=0, 0
for i in range(501,1000,2):
    hap=hap+i
print("500에서 1000까지의 홀수의 합 : " , hap)

hap = 0
num=int(input("값 입력 : "))
for i in range(1, num+1, 1):
    hap=hap+i
print("1에서 %d까지 합 : %d" %(num, hap))

for x in range(1,51):
    if (x%10 ==0):
        print("+", end="")
    else:
        print("-", end="")

x=1
while x <= 50:
    if (x%10):
        print("-", end="")
    else :
        print("+", end="")
    x+=1
print("\n")

score=[92,86,68,120,56]
for s in score:
    if (s<0 or s>100):
        break
    print(s)
print("성적처리 끝")

score=[92,86,68,120,56]
for s in score:
    if (s<0 or s>100):
        continue
    print(s)
print("성적처리 끝")

for dan in range(2, 10):
    print(dan, "단")
    for hang in range(2,10):
        print(dan, "*", hang, "=", dan*hang)
    print()

dan=2
while dan<=9:
    hang=2
    print(dan,"단")
    while hang<=9:
        print(dan, "*", hang, "=", dan*hang)
        hang +=1
    dan+=1
    print()

# i, k, guguline = 0, 0, ""
# for i in range(2,10):
#     guguline = guguline + (" #%2d단 # " %i )
#
# print(guguline)
#
# for i in range(1,10):
#     for k in range(2,10):
#         if (k==9):
#             print ( "%2d*%2d=%2d " %(k, i ,k*i))
#             break
#         print ( "%2d*%2d=%2d " %(k, i ,k*i), end="")

hap=0
a,b=0,0
while True:
    a= int(input("더할 첫 번째 수 입력 : "))
    b= int(input("더할 두 번째 수 입력 : "))
    hap=a+b
    print("%d +%d +%d" %(a,b,hap))

while True :
    a = int(input("더할 첫 번째 수 입력 : "))
    if a==0:
        break
    b= int(input("더할 두 번째 수 입력 : "))
    hap=a+b
    print("%d +%d +%d" %(a,b,hap))
print("0을 입력해서 반복문을 탈출했습니다다")

hap, i = 0,0
for i in range(1,101):
    hap+=i
    if hap>=1000:
        break
print("1~100의 합에서 최소로 1000이 넘는 위치 : " ,i)

# ch=""
# a,b=0,0
# while True :
#     a=int(input("계산할 첫 번째 수 입력 : "))
#     b=int(input("계산할 두 번째 수 입력 : "))
#     ch=input("계산할 연산자를 입력 : ")
#     if (ch=="+"):
#         c=a+b
#     elif (ch=="-"):
#         c=a-b
#     elif (ch=="/"):
#         c=a/b
#     elif (ch=="//"):
#         c=a//b
#     print(a, ch, b, "=", c, " 입니다.")

# numstr=input("숫자를 여러개 입력하세요 : ")
#
# for i in range(0, len(numstr)):
#     heartnum=int(numstr[i])
#     if (heartnum==0):
#         print("")
#     for k in range(0, heartnum):
#         if ( k==heartnum-1 ):
#             print("♥")
#             break
#         print("♥", end="")

a= int(input("1번째 숫자 : "))
b = int(input("2번째 숫자 : "))
c = int(input("3번째 숫자 : "))
d = int(input("4번째 숫자 : "))
print("합계 ==> ", a+b+c+d)

aa=[0,0,0,0]
hap=0
aa[0]= int(input("1번째 숫자 : "))
aa[1] = int(input("2번째 숫자 : "))
aa[2] = int(input("3번째 숫자 : "))
aa[3] = int(input("4번째 숫자 : "))
hap=aa[0]+aa[1]+aa[2]+aa[3]
print("합계 ==> ", hap)