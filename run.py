# 웹브라우저
import webbrowser

# 지연시간을 위한 시간 모듈
import time

#커맨드창 클리어
import os

#마우스 조작
import pyautogui

# 재생버튼 찾아서 클릭
def play():
    time.sleep(2)
    loc = pyautogui.locateOnScreen("./IMGs/play.PNG", grayscale = True, confidence = 0.8)
    if loc == None:
        print("lecture type : youtube")
        pyautogui.click(1078, 672)
    else:
        print("detected play button location : ", end = "")
        print(loc)
        pyautogui.click(pyautogui.center(loc))

# 남은시간 표시
def tleft(time_, llecs):
    lft = int(len(llecs) / 2)
    for j in range(time_):
        os.system("cls")
        print("total time : ", end = "")
        print(time_)
        print("left time : ", end = "")
        print(time_ - j)
        print("left lectures : ", end = "")
        print(lft)
        time.sleep(1)

# 강의 링크와 강의 타입 설정
# with open("../../properties/lectures.ini", "r") as lec:
with open("properties/lectures.ini", "r") as lec:
    lectures = []
    lrt = []
    while True:
        lecs = lec.readline().replace("\n", "")
        lrntime = lec.readline().replace("\n", "")
        if lecs == "":
            break
        lectures.append(lecs)
        lrt.append(lrntime)
    print("lectures : ", end = "")
    print(lectures)
    print("time : ", end = "")
    print(lrt)
    print()

# 웹페이지 접속 및 로그인
webbrowser.open(url = "https://oc.ebssw.kr/")

while True:
    if input() == "continue":
        break
    else:
        pass

leccon = lectures * 2

# 실행
for culec in range(len(lectures)):
    webbrowser.open(url = lectures[culec])
    time.sleep(3)
    lrtsp = lrt[culec].split(":")
    slt = (int(lrtsp[0]) * 60) + int(lrtsp[1])
    print("sleeptime : ", end = "")
    print(slt)
    play()

    tleft(slt, leccon)
    leccon = []

    # with open("../../properties/lectures.ini", "r") as lr:
    with open("properties/lectures.ini", "r") as lr:
        leccon = lr.readlines()

    # with open("../../properties/lectures.ini", "w") as lw:
    with open("properties/lectures.ini", "w") as lw:
        for h in range(len(leccon)):
            if h == 0 or h == 1:
                continue
            else:
                lw.write(leccon[h])

    leccon = leccon[2:]

os.system("pause")