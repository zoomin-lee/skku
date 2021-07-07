student1 = {'학번':2017310695, '이름':'이주민', '학과':'인공지능융합학과'}
print(student1)
student1['연락처']='010-5240-8135'     # student1에 연락처 추가
student1['학과']='기계공학과'            # 이미 있는 키를 사용하면 기존의 값이 변경됨
del(student1['연락처'])                # 함수를 사용하여 삭제
print(student1['학번'])
print(student1.get('학번'))
#student1['주소']                      # 에러
print(student1.get('주소'))
print(student1.get('주소', '사전에 없는 단어입니다.'))
print(student1.keys())                # dict_keys(['학번, '이름', '학과'])
print(list(student1.keys()))          # ['학번, '이름', '학과']
print(student1.values())              # dict_values([2017310695, '이주민', '기계공학과'])
print(student1.items())               # dict_items([('학번', 2017310695), ('이름', '이주민'), ('학과', '기계공학과')])
print('이름' in student1)              # True

dic = { 'boy' : '소년', 'school' : '학교', 'book' : '책'}
if 'student' in dic :
    print("사전에 있는 단어입니다.")
else:
    print("이 단어는 사전에 없습니다")

keylist = dic.keys()
for key in keylist :
    print(key)

dic2 = {'student' : '학생', 'school' : '학교', 'book' : '책'}
dic.update(dic2)
print(dic)

# 순서는 매번 바뀜
asia = {'korea', 'japan', 'china', 'korea'}                     # {'korea', 'china', 'japan'}
print(set("sanhung"))                                           # {'n', 'u', 's', 'h', 'a', 'g'}
print(set([12, 34, 56, 78]))                                    # {56, 34, 12, 78}
print(set(('이주민', '김정훈', '박성연')))                          # {'박성연', '김정훈', '이주민'}
print(set({ 'boy' : '소년', 'school' : '학교', 'book' : '책'}))   # {'boy', 'school', 'book'}
print(set())                                                    # set()

asia.add('vietnam')
asia.add('china')
asia.remove('japan')                                            # {'korea', 'china', 'vietanam'}
asia.update({'singapore', 'honkong', 'korea'})                  # {'korea', 'china', 'vietanam', 'singapore', 'honkong'}

twox = {2,4,6,8,10,12}
threex={3,6,9,12,15}
print("교집합", twox & threex)
print("합집합", twox | threex)
print("차집합", twox - threex)
print("차집합", threex - twox)
print("배타적 차집합", twox ^ threex)

score = [88,95,70,100,90]
for no, s in enumerate(score, 1):
    print(str(no)+"번 학생의 성적 : " , s)

yoil = ["월", "화", "수", "목", "금", "금", "토", "일"]
food = ["갈비탕", "순대국", "칼국수", "삼겹살"]
menu = zip(yoil, food)
for y, f in menu:
    print("%s 요일 메뉴 : %s" %(y,f))

adult = [True, False, True, False]
print(any(adult))
print(all(adult))

score = [45,80,70,53,95]
def flunk(s):
    return s<60
for s in filter(flunk, score):
    print(s)

def half(s):
    return s/2
for s in map(half,score):
    print(s, end=' ')
print()

score = [45,80,70,53,95]
for s in filter(lambda x:x < 60, score):
    print(s)

list1 = [1,2,3]
list2 = list1
list3 = list1.copy()
print("1 == 2" , list1 is list2)
print("1 == 3" , list1 is list3)
print("2 == 3" , list2 is list3)