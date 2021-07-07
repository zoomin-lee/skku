score = [88,95,70,100,99]
sum=0
for s in score :
    sum+=s
print("총점 : ", sum)
print("평균 : ", sum/len(score))

nums=[0,1,2,3,4,5,6,7,8,9]
print(nums[1:7:2])          #[1,3,5]
nums[2:5]=[20,30,40]        #[0,1,20,30,40,5,6,7,8,9]
nums[6:8]=[90, 91, 92, 93, 94]      #[0,1,20,30,40,5,90,91,92,93,94,8,9]

lol=[[1,2,3],[4,5],[6,7,8,9]]
for sub in lol:
    for item in sub:
        print(item, end= ' ')
    print()

nums = [n*2 for n in range(1,11)]
for i in nums:
    print(i, end=' ')
print()
nums.insert(2,99)

list1=[1,2,3,4,5]
list2=[10,11]
listadd = list1+list2   #[1,2,3,4,5,10,11]
listmuti = list2*3      #[10,11,10,11,10,11]

score = [[88, 76,92,98],[65,70,58,82],[82,80,78,88]]
total, totalsub=0,0
for student in score :
    sum=0
    for subject in student :
        sum+=subject
    subjects=len(student)
    print("총점 %d, 평균 %.2f" %(sum, sum/subjects))
    total+=sum
    totalsub +=subjects
print("전체평균 %.2f" %(total / totalsub))

nums=[1,2,3,4]
nums[2:2]=[90,91,92]    #[1, 2, 90, 91, 92, 3, 4]

nums=[1,2,3,4]
nums[2]=[90,91,92]      #[1, 2, [90, 91, 92], 4]

list1=[1,2,3,4,5]
list2=[10,11]
list1.extend(list2)     # [1, 2, 90, 91, 92, 3, 4]

score = [88,95,70,100,99,80,78,50]
score.remove(100)       # [88,95,70,99,80,78,50]
del(score[2])           # [88,95,99,80,78,50]
score[1:4]=[]           # [88,78,50]

score = [88,95,70,100,99]
print(score.pop())      # 99
print(score.pop())      # 100
print(score.pop(0))     # 88
print(score)            # [95,70]

score = [88,95,70,100,99,80,78,50]
perfect = score.index(100)
print("만점 받은 학생은 "+str(perfect)+"번입니다.")
pernum = score.count(100)
print("만점자 수는 "+str(pernum)+"명입니다")
print("학생 수는 %d명 입니다." %len(score))
print("최고 점수는 %d점 입니다." %max(score))
print("최저 점수는 %d점 입니다." %min(score))

ans=input("결제 하시겠습니까?")
if ans in ['yes', 'y', 'ok', '예', '당근']:
    print("구입해 주셔서 감사합니다.")
else:
    print("안녕히 가세요")

score = [88,95,70,100,99]
score.sort()         # [70, 88, 95, 99, 100]
score.reverse()      # [100, 99, 95, 88, 70]
score2=sorted(score) # [70, 88, 95, 99, 100]

country=['Korea', 'japan', 'CHINA', 'america']
country.sort()       # ['CHINA', 'Korea', 'america', 'japan']
country.sort(key=str.lower)     # ['america', 'CHINA', 'japan', 'Korea']

score = (88,95,70,100,99)
sum=0
for s in score:
    sum+=s
print("총점 : ", sum)
print("평균 : ", sum/len(score))

tu=1,2,3,4,5
print(tu[3])
print(tu[1:4])
print(tu+(6,7))
print(tu * 2)
# tu[1]=100     # 튜플은 변경 불가
# del tu[1]     # 튜플은 삭제 불가

aa = "이순신", "김유신","강감찬"
lee, kim, kang = aa
print(lee)
print(kim)
print(kang)

import time
def gettime():
    now=time.localtime()
    return now.tm_hour, now.tm_min
result=gettime()
print("지금은 %d시 %d분입니다"%(result[0], result[1]))

d, m = divmod(7,3)      # 나눗셈의 몫과 나머지를 튜플로 묶어 리턴
print("몫", d)
print("나머지", m)

score=[88,95,70,100,99]
tu=tuple(score)         # list -> tuple
print(tu)
li = list(tu)           # tuple -> list
li[0]=100
print(li)

aa=[]
for i in range(0,100):
    aa.append(i)
print(len(aa))

for i in range(0,4):
    aa[i]=int(input(str(i+1)+"번째 숫자 : "))
hap=aa[0]+aa[1]+aa[2]+aa[3]
print("합계 ==> ", hap)