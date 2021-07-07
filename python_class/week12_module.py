import math
print(math.sqrt(2))

from math import sqrt
print(sqrt(2))

import math as m
print(m.sqrt(2))

from math import sqrt as sq
print(sq(2))

import math
print(math.sin(math.radians(45)))
# sin 삼각함수를 계산, 인수 x는 라디안 값
# randians() 각도를 라디안 값으로 바꾼다

print(math.sqrt(2))
print(math.factorial(5))

# import turtle as t
# t.penup()
# t.goto(-720,0)
# t.pendown()
# for x in range(-720,720):
#     t.goto(x, math.sin(math.radians(x))*100)
# t.done()

import statistics
score=[30,40,60,70,80,90]
print(statistics.mean(score))
print(statistics.harmonic_mean(score))
print(statistics.median(score))
print(statistics.median_low(score))
print(statistics.median_high(score))

import time
t=time.time()
print(t)
print(time.ctime(t))
print(time.localtime(t))
now = time.localtime()
print("%d년 %d월 %d일" %(now.tm_year, now.tm_mon, now.tm_mday))
print("%d:%d:%d" %(now.tm_hour, now.tm_min, now.tm_sec))

import datetime
now = datetime.datetime.now()
print("%d년 %d월 %d일" %(now.year, now.month, now.day))
print("%d:%d:%d" %(now.hour, now.minute, now.second))

import time
start = time.time()
for a in range(1000):
    print(a)
end = time.time()
print(end-start)

print("안녕하세요")
time.sleep(1)
print("밤에 성시경이 두명 있으면 될까요?")
time.sleep(1)
print("야간 투시경입니다.")

for dan in range(2,10):
    print(dan, '단')
    for hang in range(2,10):
        print(dan, "*", hang, "=", dan*hang)
        time.sleep(0.001)
    print()
    time.sleep(0.005)

import calendar
print(calendar.calendar(2020))
print(calendar.month(2021,1))
calendar.prcal(2020)
calendar.prmonth(2021,1)

yoil = ['월','화','수','목','금','토','일']
day = calendar.weekday(2020,8,15)
#요일을 숫자로 바꿔줌 즉 5->yoil[5]=토
print("광복절은" , yoil[day], "요일이다")

import random
for i in range(5):
    print(random.random())          # 0<= x <1까지의 난수
for i in range(5):
    print(random.randint(1,10))     # 1<= x <=10까지의 정수 난수
for i in range(5):
    print(random.uniform(1,100))    # 1<= x <100 까지의 난수

food = ["짜장면","짬뽕","탕수육","군만두"]
print(random.choice(food))
print(food)
random.shuffle(food)
print(food)
print(random.sample(food,2))

nums = random.sample(range(1,46),6)
nums.sort()
print(nums)

a=random.randint(1,9)
b=random.randint(1,9)
question = "%d + %d = ?" %(a,b)
c=int(input(question))
if c == a+b:
    print("정답입니다")
else :
    print("틀렸습니다")
