print(0b10010011)
print(int('10010011',2))
print(int('93',16))
a=bin(13)
b= bin(0x13)
c= bin(0xC5F7)
print(a)
print(b)
print(c)

# a = int(input("입력진수 결정(16/10/8/2) : "))
# num = input("값 입력 : ")
# num10=int(num,a)
#
# x= bin(num10)
# y= oct(num10)
# z= hex(num10)
#
# print("16진수 ==> ",z)
# print("10진수 ==>", num10)
# print("8진수 ==>", y)
# print("2진수 ==>", x)

a=123
print(type(a))

a=100**100
print(a)

a=0xFF #16진수
b=0o77 #8진수
c=0b1111 #2진수
print(a,b,c)

a=3.14
b=3.14e5
print(a,b)

a=10
b=20
print(a+b, a-b, a*b, a/b)

a,b=9,2
print(a**b) #9의 2승
print(a%b) #나머지
print(a//b) #몫

a=True
print(type(a))

a=(100==100)
b=(10>100)
print(a,b)

a="파이썬 만세"
a
print(a)
type(a)

b = "작은 따옴표 모양은 ' 입니다"
c= ' 큰 따옴표 모양은 " 입니다'
d= '작은 따옴표 모양은 \' 입니다'
e = " 큰 따옴표 \" 모양은 입니다"
print(b)
print(c)
print(d)
print(e)

a= '파이썬 \n 만세'
print(a)

a= """파이썬
만세"""
print(a)

a=123456789
print(a)
print(a**100)

a=0x1a #16진수 ,a=10
print(a)

a=0b1101
print(a)

print(hex(26))
print(oct(26))
print(bin(13))

a=9.46e12
print(a)

a=1+2j
b=3+4j
print(a+b)

a = "Korea 서울 1234"
print(a)

a='I Say "Help" to you'
print(a)

a= 'I Say \'help\' to you'
print(a)

a= "first\nsecond"
print(a)

a="first\tsecond"
print(a)

a="first\"second"
print(a)

a="first\\second"
print(a)

a= "old\new"
print(a)

a= "old\\new"
print(a)

a= "old//new"
print(a)

a= "old/new"
print(a)

a= "old\nnew"
print(a)

a= """old
new"""
print(a)

s="""강나루 건너서 밀밭 길을 구름에 달 가듯이 가는 나그네
길은 외줄기 남도 삼백리 술 익는 마을보다 타는 저녁놀
구름에 달 가듯이 가는 나그네"""
print(s)

s="강나루 건너서 밀밭 길을 구름에 달 가듯이 가는 나그네\
길은 외줄기 남도 삼백리 술 익는 마을보다 타는 저녁놀\
구름에 달 가듯이 가는 나그네"
print(s)

totalsec = 365*24*\
           60*60
print(totalsec)

s= "korea""japan""2002"
print(s)

s="korea    japan   2002"
print(s)

s=("korea"
   "japan"
   "2002")
print(s)

print(ord('A')) #아스키 코드 index
print((98))
print(98)

for c in range(ord('A'), ord('Z')+1):
    print(chr(c),end=' ')

a=5
b=a==5
print(b)

a=5
if a==5:
    print("a는 5입니당.")

a=None
print(a)

member=['손오공','저팔계','사오정','삼장법사']
for m in member:
    print(m, " 출동")

# a = int(input("첫번째 숫자를 입력하세요 :  "))
# b = int(input("두번째 숫자를 입력하세요 : "))
#
# print(a, "+", b, "=", a + b)
# print(a, "-", b, "=", a-b)
# print(a, "*", b, "=", a * b)
# print(a, "/", b, "=",  a / b)

# money = int(input("교환할 돈은 얼마? "))
# c500 = money // 500
# money %= 500
#
# c100=money//100
# money %=100
#
# c50=money//50
# money %=50
#
# c10=money//10
# money %= 10
#
# print("오백원짜리 ==> ", c500, "개")
# print("백원짜리 ==> ", c100, "개")
# print("오십원짜리 ==> ", c50, "개")
# print("십원짜리 ==> ", c10, "개")
# print("바꾸지 못한 잔돈 ==> ", money, "원" )
