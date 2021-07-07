a=3
s='korea'
f=3.1415
e=5
d=3
c=2

a=(1+2)*3
b=c*d+e
print(a)
print(b)

a=5/2
b=5//2
print(a)
print(b)

a=7%2
b=8%3
c=9%3
print(a)
print(b)
print(c)

a=5
a=a+1
print(a)
a+=1
print(a)

s1="대한민국"
s2="만세"
print(s1+s2)
print("좋아"*5)

#print("korea"+2002)
print("korea"+str(2002))
print(10+int("22"))

print(10+float("22.5"))
print(10+float("314e-2"))

print(int(2.54))
print(round(2.54))
print(round(2.54,1))
print(round(2.56,1))
print(round(123456, -3))
print(round(123656, -3))

age=int(input("연령이 어떻게 됩니까?"))
if age<19:
    print("미성년입니다")
if age>19:
    print("성인입니다")

a=int(input("a는 몇인가?"))
if a==3:
    print("3이다")
if a>5:
    print("5보다 크다")
if a<5:
    print("5보다 작다")

country="KOREA"
if country=="KOREA":
    print("한국입니다")
if country =="korea":
    print("대한민국입니다")

if("k">"j"):
    print("k")  # k가 j보다 뒤에 위치
if("k"<"j"):
    print("j")  #알파벳 순서에 따라 대소 비교 가능함!!!

if("korea">"japan"):
    print("한국이 더 크다")
if("korea"<"japan"):
    print("일본이 더 크다")

energy=1
if energy:
    print("열심히 공부한당")

a=3
if a>1 and a<10:
    print("ok")

age=16
if age<19:
    print("열심히 공부한다.")
    print("공부 열심히 해야지")

age=24
if age<19:
    print("열심히 공부한다.")
print("공부 열심히 해야지")

age=22
if age<19:
    print("열심히 공부한다")
else :
    print("공부 열심히 해야지")

age=20
if age<19:
    print("열심히 공부한다")
if age>19:
    print("훌륭한 사람이 될 겁니다")

age=23
if age<19:
    print("미성년 입니다")
elif age<25 :
    print("성년입니다")
else :
    print("청장년층입니다")

Grades=90
if Grades>=90:
    print("A")
elif Grades>=80:
    print("B")
elif Grades>=70:
    print("C")
elif Grades>=60:
    print("D")
else:
    print("F")

man =True
age=22
if man ==True:
    if age>=19:
        print("성인 남자입니다.")

man=True
age=int(input("나이가 몇살입니까?"))
if man==True :
    if age>= 19:
        print("성인 남자입니다")
    else :
        print("소년입니다")
else:
    if age>= 19:
        print("성인 여자입니다")
    else :
        print("소녀입니다")

a=200
if a<100 :
    print("100보다 작군요")
print("거짓이므로 이 문장은 안 보이겠죠?")
print("프로그램 끝")

a=200
if a<100 :
    print("100보다 작군요")
    print("거짓이므로 이 문장은 안 보이겠죠?")
print("프로그램 끝")

a=int(input("정수를 입력하세요:"))
if a%2==0:
    print("짝수를 입력했군요")
else :
    print("홀수를 입력했군요")

a=75
if a>50:
    if a<100:
        print("50보다 크고 100보다 작군요")
    else:
        print("100보다 크군요")
else :
    print("50보다 작군요")

a=int(input("첫번째 수를 입력하세요: "))
ch=input("계산할 연산자를 입력하세요: ")
b=int(input("두번째 수를 입력하세요: "))

if ch=="+":
    print("%d + %d = %d 입니다." %(a,b,a+b))
elif ch=="=":
    print("%d = %d 입니다" %(a,b))
elif ch=="-":
    print("%d - %d = %d 입니다." %(a,b,a-b))
elif ch=="*":
    print("%d * %d = %d 입니다." %(a,b,a*b))
elif ch=="**":
    print("%d ** %d = %d 입니다." %(a,b,a**b))
elif ch=="%":
    print("%d %% %d = %d 입니다." %(a,b,a%b))
elif ch=="//":
    print("%d // %d = %d 입니다." %(a,b,a//b))
