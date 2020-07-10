# 웹브라우저
import webbrowser

# 지연시간
import time

#커맨드창 클리어
import os

#마우스 조작
import pyautogui

# 재생버튼 찾아서 클릭
def play():
    time.sleep(2)
    loc = pyautogui.locateOnScreen("IMGs/play.PNG", grayscale = True, confidence = 0.8)
    if loc == None:
        loc = pyautogui.locateOnScreen("IMGs/play2.PNG", grayscale = True, confidence = 0.5)

        if loc == None:
            print("lecture type : youtube")
            pyautogui.click(1078, 672)

        else:
            print("detected play button2 location : ", end="")
            print(loc)
            pyautogui.click(pyautogui.center(loc))
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
        print(time_, end = "")
        print(" seconds")
        print("left time : ", end = "")
        print(time_ - j, end = "")
        print(" seconds")
        print("left lectures : ", end = "")
        print(lft)
        time.sleep(1)

# 강의 링크와 시간 설정
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
    min = int(lrtsp[0])
    sec = lrtsp[1]
    if sec.find("!") != -1:
        sec = int(sec.replace("!", ""))
        slt = int(((min * 60) + sec) * 0.7)
    else:
        slt = ((min * 60) + int(sec))
    print("sleeptime : ", end = "")
    print(slt)
    play()

    tleft(slt, leccon)
    leccon = []

    with open("properties/lectures.ini", "r") as lr:
        leccon = lr.readlines()

    with open("properties/lectures.ini", "w") as lw:
        for h in range(len(leccon)):
            if h == 0 or h == 1:
                continue
            else:
                lw.write(leccon[h])

    leccon = leccon[2:]

os.system("pause")