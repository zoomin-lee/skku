# class Car :
#     color=''
#     speed=0
#     def upspeed(self,value):
#         self.speed +=value
#     def downspeed(self,value):
#         self.speed -=value
# mycar1 = Car()
# mycar1.color = "빨간색"
# mycar1.speed=0
#
# mycar2 = Car()
# mycar2.color="노란색"
# mycar2.speed=10
#
# mycar3 = Car()
# mycar3.color="파란색"
# mycar3.speed=20
#
# mycar1.upspeed(30)
# print("자동차 1의 색상은 %s이며, 현재속도는 %d km 입니다."%(mycar1.color, mycar1.speed))
#
# mycar2.upspeed(30)
# print("자동차 2의 색상은 %s이며, 현재속도는 %d km 입니다."%(mycar2.color, mycar2.speed))
#
# mycar3.upspeed(30)
# print("자동차 3의 색상은 %s이며, 현재속도는 %d km 입니다."%(mycar3.color, mycar3.speed))
#
# class Car:
#     color = ''
#     speed=0
#     def __init__(self):
#         self.color = "빨강"
#         self.speed =0
#     def upspeed(self,value):
#         self.speed +=value
#     def downspeed(self,value):
#         self.speed-=value
#
# mycar1 = Car()
# mycar2 = Car()
#
# print("자동차1의 색상은 %s이며, 현재속도는 %d km입니다." %(mycar1.color, mycar1.speed))
# print("자동차2의 색상은 %s이며, 현재속도는 %d km입니다." %(mycar2.color, mycar2.speed))
#
# class Car :
#     color =""
#     speed = 0
#     def __init__(self, value1, value2):
#         self.color = value1
#         self.speed = value2
#
#     def upSpeed(self, value):
#         self.speed += value
#
#     def downSpeed(self, value):
#         self.speed -= value
# mycar1=Car("빨강", 30)
# mycar2 = Car("노랑", 60)
#
# print("자동차 1의 색상은 %s 이며, 현재속도는 %d km 입니다. " %(mycar1.color, mycar1.speed))
# print("자동차 2의 색상은 %s 이며, 현재속도는 %d km 입니다. " %(mycar2.color, mycar2.speed))
#
# class Car :
#     color =""
#     speed = 0
#     count = 0
#
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
#         Car.count += 1
#
#     def getName(self):
#         return self.name
#
#     def getSpeed(self):
#         return self.speed
# mycar1=Car("아우디", 30)
# mycar2 = Car("벤츠", 60)
#
# print(" %s의 현재속도는 %d km 입니다. " %(mycar2.getName(), mycar2.getSpeed()))
#
# class Car :
#     color =""
#     speed = 0
#     count = 0
#
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
#         Car.count += 1
#
#     def getSpeed(self):
#         return self.speed
#
# mycar1=Car("아우디", 30)
# print("자동차 1의 현재속도는 %d km, 생성된 자동차 숫자는 총 %d대 입니다. " %(mycar1.speed, Car.count))
# mycar2 = Car("벤츠", 60)
# print("자동차 2의 현재속도는 %d km, 생성된 자동차 숫자는 총 %d대 입니다. " %(mycar2.speed, Car.count))

# class Car :
#     speed = 0
#     def upSpeed(self, value):
#         self.speed += value
#     def downSpeed(self, value):
#         self.speed -= value
#
# class Sedan(Car):
#     seatNum = 0
#     def getSeatNum(self):
#         return self.seatNum
# class Truck(Car):
#     capacity = 0
#     def getCapcity(self):
#         return self.capacity
#
# sedan1 = Sedan()
# truck1 = Truck()
#
# sedan1.upSpeed(100)
# truck1.upSpeed(80)
#
# sedan1.seatNum=5
# truck1.capacity = 50
#
# print("승용차의 속도는 %d km, 좌석수는 %d개 입니다." %(sedan1.speed, sedan1.getSeatNum()))
# print("트럭의 속도는 %d km, 총중량은 %d톤 입니다." %(truck1.speed, truck1.getCapcity()))

class Car :
    speed = 0
    def upSpeed(self, value):
        self.speed += value
        print("현재 속도 ( 슈퍼 클래스 ) : %d" %self.speed)

class Sedan(Car):
    def upSpeed(self, value):
        self.speed += value
        if self.speed > 150 :
            self.speed=150
        print("현재 속도 ( 서브 클래스 ) : %d" %self.speed)

class Truck(Car):
    pass

truck1 = Truck()
sedan1 = Sedan()
print("트럭 --> ", end='')
truck1.upSpeed(200)
print("승용차 --> ", end='')
sedan1.upSpeed(200)

str = "89점"
try :
    score = int(str)
    print(score)
except :
    print("예외가 발생했습니다")
print("작업완료")

str = "89"
try :
    score = int(str)
    print(score)
    a = str[5]
except ValueError:
    print("점수의 형식이 잘못되었습니다.")
except IndexError:
    print("첨자 범위를 벗어났습니다.")
print("작업완료")

while True :
    str = input("점수를 입력하세요 : ")
    try :
        score = int(str)
        print("입력한 점수 : ", score)
        break
    except :
        print("점수 형식이 잘못되었습니다.")
print("작업완료")

str = "89w"
try :
    score = int(str)
    print(score)
    a = str[5]
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)
print("작업완료")

def calcsum(n):
    if (n<0):
        raise ValueError
    sum =0
    for i in range(n+1):
        sum+=i
    return sum
try :
    print("~10 = ",calcsum(10))
    print("~-5 = ",calcsum(-5))
except ValueError:
    print("입력값이 잘못되었습니다")


##################시험문제####################
def calcsum(n):
    if (n<0):
        return -1
    sum=0
    for i in range(n+1):
        sum+=i
    return sum
result = calcsum(10)
if result == -1:
    print("입력값이 잘못되었습니다.")
else:
    print("~10 = ", result)

result = calcsum(-4)
if result == -1:
    print("입력값이 잘못되었습니다.")
else:
    print("~10 = ", result)
###################################################

dic = {'boy':'소년','school':'학교', 'book':'책'}
try :
    print(dic['girl'])
except :
    print("찾는 단어가 없습니다")

han = dic.get("girl")
if (han == None):
    print("찾는 단어가 없습니다.")
else :
    print(han)

try :
    print("네트워크 접속")
    a=2/0
    print("네트워크 통신 수행")
finally:
    print("접속해제")
print("작업완료") # print 안됨

score=128
assert score <= 100, "점수는 100이아여야 합니다"
print(score)