2+3
print(2+3)

for y in range(1,10):
    for x in range(y) :
        print('*', end= ' ')
    print()

value=1234
print(value)
print(value*2)

s= "서울"
d= "대전"
g= "대구"
b = "부산"
print(s,d,g,b, sep= '찍고')

a='강아지'
b='고양이'
print(a)
print(b)

print(a, end='')
print(b)

print(12, 34, 56, sep='^^', end='-->')

age = input('몇 살이세요?')
print(age)

price=input('가격을 입력하세요 : ')
num=input('개수를 입력하세요 : ')
sum= int(price)*int(num)
print('총액은', sum, ' 원입니다')
print()

price=int(input('가격을 입력하세요 : '))
num=int(input('개수를 입력하세요 : '))
sum= price*num
print('총액은', sum, ' 원입니다')

score= 98
print(score)

score='high'
print(score)

name=input('이름을 입력하세요 : ')
print('안녕하세요', name, '님')

print('안녕하세요?')

print('100')
print("%d" % 100)

print("100+100") #글자
print("%d" % (100+100)) #숫자

print("%d %d" % (100,200))
#print("%d" % (100,200))
#print("%d %d" % (200))

#print("%d/%d=%d" % (100,200,0.5))
print("%d/%d=%d" % (200,100,2))
print("%d/%d=%5.1f" % (100,200,0.5))

print("%d" % 123)
print("%5d" % 123)
print("%05d" % 123)

print("%f" % 123.45)
print("%7.1f" % 123.45)
print("%7.3f" % 123.45)

print("%s" % "Python")
print("%10s" % "Python")

print("\n줄바꿈\n연습")
print("\t탭키\t연습")
print("글자가\"강조\"되는 효과1")
print("글자가\'강조\'되는 효과2")
print("\\\\\\ 역슬래쉬 세개 출력")
print(r"\n \t \" \\를 그대로 출력")

print("%d %5d %05d" % (123, 123, 123))
print("{1:d} {2:5d} {0:05d}".format(123,123,123))