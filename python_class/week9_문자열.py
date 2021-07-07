s="python"
print(s[2])
print(s[-2])

for c in s:
    print(c, end=',')

print(s[2:5])
print(s[3:])
print(s[:4])
print(s[2:-2])

file='20201102-182230.jpg'
print("촬영 날짜 : "+file[4:6]+"월 "+ file[6:8]+"일")
print("촬영 시간 : "+file[9:11]+"시 "+ file[11:13]+"분")
print("확장자 : "+file[-3:])

yoil = "월화수목금토일"
print(yoil[::2])
print(yoil[::-1])

s="python programming"
print(len(s))       # 18
print(s.find('o'))  # 4
print(s.rfind('o')) # 9 뒤에서 검색 시작
print(s.index('r')) # 8
print(s.count('o')) # 2

s="""생각이란 생각할수록 생각나므로 생각하지 말아야 할 생각은 생각하지
않으려고 하는 생각이 옳은 생각이라고 생각합니다."""
print("생각의 출현 횟수 : ", s.count("생각"))

s="python programming"
print('a' in s)     # True
print('z' in s)     # False
print('pro' in s)   # True
print('x' not in s) # True

name = "김한결"
if name.startswith("김"):
    print("김가입니다")
if name.startswith("한"):
    print("한가입니다.")

file= "girl.jpg"
if file.endswith(".jpg"):
    print("그림 파일입니다.")

# 앞에 is가 붙은 함수는 F,T로 결과가 나옴
# isalpha : 모든 문자가 알파벳인지 조사
# islower : 모든 문자가 소문자인지 조사
# isupper : 모든 문자가 대문자인지 조사
# isspace : 모든 문자가 공백인지 조사
# isalnum : 모든 문자가 알파벳 또는 숫자인지 조사
# isdecimal / isdigit / isnumeric : 모든 문자가 숫자인지 조사
# isidentifier : 명칭으로 쓸 수 있는 문자로만 구성되어 있는지 조사
# isprintable : 인쇄 가능한 문자로만 구성되어 있는지 조사

height = input("키를 입력하세요 : ")
if height.isdecimal():
    print("키 = ", height)
else :
    print("숫자만 입력하세요.")

s="Good morning. my love KIM"
print(s.lower())        # 각기 영문자를 전부 소문자로 바꿈. s에 영향은 없음
print(s.upper())        # 각기 영문자를 전부 대문자로 바꿈. s에 영향은 없음
print(s)

print(s.swapcase())     # 대문자 -> 소문자, 소문자 -> 대문자. s에 영향은 없음
print(s.capitalize())   # 단어의 첫글자를 대문자로 바꿈. s에 영향은 없음
print(s.title())        # 첫단어의 첫글자만 대문자로 바꿈. s에 영향은 없음
print(s)

python = input("파이썬의 영문 철자를 입력하시오 : ")
if python.lower()=="python":
    print("맞췄습니다")

s="     angel   "
print(s+"님")
print(s.lstrip()+"님")   # 왼쪽의 공백 제거
print(s.rstrip()+"님")   # 오른쪽의 공백 제거
print(s.strip()+"님")    # 양쪽의 공백 제거

# split method : 구분자를 기준으로 문자열을 구분
s="짜장 짬뽕 탕수육"
print(s.split())

s2="서울->대전->대구->부산"
city = s2.split("->")
print(city)

for c in city:
    print(c, "찍고", end=' ')
print()

# splitlines() : 개행 문자나 파일 구분자 등 기준으로 문자열을 잘라 리스트로 만듦
traveler = """강나루 건너서 \n밀밭 길을 \n\n구름에 달 가듯이 \n가는 나그네\n
길은 외줄기 \n남도 삼백리\n\n술 익는 마을마다 \n타는 저녁놀\n
구름에 달 가듯이 \n가는 나그네"""
poet = traveler.splitlines()
for line in poet:
    print(line.center(30))

# join() : 문자열의 각 문자 사이에 다른 문자열을 끼워넣음
s="._."
print(s.join("대한민국"))

s2="서울->대전->대구->부산"
city = s2.split("->")
print(" 찍고 ".join(city))

ss = "python을 열심히 공부 중"
print(ss.split())
ss="하나:둘:셋"
print(ss.split(":"))
ss="하나\n둘\n셋"
print(ss.splitlines())
ss="%"
print(ss.join("파이썬"))

ss=input("날짜(연/월/일) 입력 ==> ")
ssList=ss.split('/')
print("입력한 날짜의 10년 후 ==> ", end='')
print(str(int(ssList[0])+10)+"년 ", end='')
print(ssList[1] + "월 ", end='')
print(ssList[2] +"일")


value = 123
print("###%d###" %value)    # ###123###
print("###%5d###" %value)   # ###  123###
print("###%10d###" %value)  # ###       123###
print("###%1d###" %value)   # ###123###

price = [30,13500,2000]
for p in price :
    print("가격 : %d원" %p)
for p in price:
    print("가격 :%7d원" %p)
for p in price :
    print("가격 : %-7d원" %p)  # 앞에 숫자를 채우고 나머지 부분을 빈공간으로

pie = 3.14159265
print("%10f" %pie)
print("%10.8f" %pie)
print("%10.5f" %pie)
print("%10.2f" %pie)        # .2면 소수점 셋째 자리에서 반올림

ss = '파이썬 짱!'
sslen = len(ss)
for i in range(0,sslen):
    print(ss[i]+'$', end='')
print()

s="독도는 일본땅이다. 대마도도 일본땅이다"
print(s)
print(s.replace("일본", "한국"))    # replace 첫번째 인수는 검색할 문자열 지정, 두번째 인수는 바꿀 문자열 지정

message = "안녕하세요"
print(message.ljust(30))    # 왼쪽 정렬
print(message.rjust(30))    # 오른쪽 정렬
print(message.center(30))   # 중앙 정렬


outStr=""
inStr = input("문자열을 입력하세요 : ")
count = len(inStr)
for i in range(0, count) :
    outStr += inStr[count-(i+1)]
print("내용을 거꾸로 출력 --> %s" %outStr)


ss=input("문자열 입력 ==>")
print("출력 문자열 ==> ", end='')
if ss.startswith('(') == False :
    print("(", end=' ')
print(ss, end='')
if ss.endswith(')') == False :
    print(" )", end=' ')
print()

ss="   파  이  썬   "  # 단, 가운데는 제거되지 않음
ss.strip()      # 문자열의 양쪽 공백 제거
ss.rstrip()     # 문자열의 오른쪽 공백 제거
ss.lstrip()     # 문자열의 왼쪽 공백 제거

ss='---파---이---썬----'
print(ss.strip("-"))    # 문자열의 양쪽 - 제거
ss="<<<파 << 이 >> 썬 >>>"
print(ss.strip("<<<"), end="")
print()
print(ss.strip("<>"), end="")
print()
print(ss.strip("><"), end="")
print()

inStr = "    한글   PYTHON    프로그래밍   "
outStr = ""
for i in range(0, len(inStr)):
    if inStr[i] != " ":
        outStr += inStr[i]
print("원래 문자열 ==> "+ '[' + inStr +']')
print("공백 제거 ==> "+ '[' + outStr + ']')

ss = input("문자열 입력 ==>")
print("출력 문자열 ==> ", end ='')
for i in range(0, len(ss)):
    if ss[i] != 'o' :
        print(ss[i], end='')
    else :
        print("$", end='')

before=['2019', '12', '31']
after=list(map(int,before))
print(after)

ss='파이썬'
print(ss.zfill(10))     # 0000000파이썬

inStr = input("문자열을 입력하세요 : ")
count = len(inStr)
outStr =""
for i in range(0, count):
    ch = inStr[i]
    if (ord(ch) >= ord("A") and ord(ch) <= ord("Z")):
        newCh=ch.lower()
    elif (ord(ch) >= ord("a") and ord(ch) <= ord("z")):
        newCh=ch.upper()
    else:
        newCh=ch
    outStr += ch
print("대소문자 변환 결과 --> %s" %outStr)