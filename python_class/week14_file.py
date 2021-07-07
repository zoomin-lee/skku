f = open("live.txt", "wt")
f.write("""삶이 그대를 속일지라도
슬퍼하거나 노하지 말라!
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리니""")
f.close

try:
    f = open("live.txt", "rt")
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()


f = open("live.txt", "rt")
text =""
line=1
while True :
    row = f.readline()
    if not row : break
    text += str(line) +" : "+ row
    line+=1
f.close()
print(text)

f = open("live.txt", "rt")
f.seek(12,0) # 위치(12byte를 건너뛰고, 한글은 2byte 공백도 포함)
            # 기준(0:처음부터 2:끝부터 1:현재위치부터)
text = f.read()
f.close()
print(text)

# a 모드 : 기존 내용 그대로 유지하고 뒤에 덧붙임
# w 모드 : 파일 이미 있는 경우 덮어쓰고 새로 만듦
f = open("live.txt", "at")
f.write("\n\n푸쉬킨 형님의 말씀이었습니다.")
f.close()

with open("live.txt","rt") as f:
    text = f.read()
print(text)


# 디렉토리, 서브 디렉토리까지 전부 복사
import shutil
shutil.copy("live.txt", "live2.txt")

import os
files = os.listdir("C:\\Users\jumin\PycharmProjects\pythonProject\python")
for f in files:
    print(f)

def dumpdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = path+"\\"+f
        if os.path.isdir(fullpath):
            print("["+fullpath+"]")
            dumpdir(fullpath)
        else :
            print("\t" +fullpath)
dumpdir("C:\\Users\jumin\PycharmProjects\pythonProject")

inFP = open("C:/Temp/data1.txt","r",encoding="utf-8")
while True :
    inStr = inFP.readline()
    if inStr =="":
        break
    print(inStr, end="")
print("")
inFP.close()

inFP = open("C:/Temp/data1.txt","r",encoding="utf-8")
inList=inFP.readlines()
print(inList)
for inStr in inList:
    print(inStr, end="")
inFP.close()


fName = input("파일명을 입력하세요 : ")
inFP = open(fName,"r",encoding='utf-8')
inList = inFP.readlines()
for inStr in inList:
    print(inStr, end="")
inFP.close()