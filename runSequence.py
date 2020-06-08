# 正式服
import cv2
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
from time import sleep
from sys import exit
import os

pyautogui.FAILSAFE = False # 触碰到边界不报错
pyautogui.PAUSE = 0.5 # 执行一个动作的时长

waiteTime = 10
cycle = 100
maxFindTimes = 1000
events = []

# 点击原点位置
print('请在 5s 内把鼠标指针移动到原点')
sleep(5)
baseX,baseY = pyautogui.position()
print("当前鼠标位置为： ",(baseX,baseY))
go = input("是否继续执行脚本？ y/n")
if go == "n":
    exit(1)

# 模板匹配算法
def getTemplatePosition(templatePath):
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    meth = methods[1]
    method = eval(meth)
    x = baseX - 483
    y = baseY - 574
    w = 967
    h = 611
    img = pyautogui.screenshot(region=(x,y, w,h)) #x,y,w,h 这里的常量是测量 seer 怀旧服登录器 得到的
    img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
    template = cv2.imread(templatePath,0)
    w, h = template.shape[::-1]
    template = cv2.cvtColor(np.asarray(template),cv2.COLOR_RGB2BGR)
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return (x + top_left[0] + w//2, y + top_left[1] + h//2)


path = "sequence" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
s = []
for file in files: #遍历文件夹
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
        # 读取动作序列
        print(path+"/"+file)
        with open(path+"/"+file,"r",encoding='utf8') as f:
            argvs = f.readline().replace('\n','').split("\t") 
            try:
                argvs = list(map(int,argvs))
            except:
                pass
            argc = 0

            try :
                waiteTime = argvs[argc]
            except :
                waiteTime = 10
            
            argc += 1 
            try :
                cycle = argvs[argc]
            except :
                cycle = 100

            argc += 1 
            try :
                maxFindTimes =argvs[argc]
            except :
                maxFindTimes = 1000


            for eachLine in f:
                event = eachLine.replace('\n','').split("\t") 
                try :
                    event[0:2] = map(int,event[0:2])
                except :
                    pass
                events.append(event)
            print(events)
        currentCycle = 0
        while currentCycle < cycle:
            for event in events:
                print(event[-1])
                if isinstance(event[0],int):
                    # 这是个坐标，直接点击
                    pyautogui.click(baseX + event[0], baseY + event[1])

                else:
                    # 这是个图片（一般是精灵），需要去找
                    pyautogui.click(getTemplatePosition('pic/' + event[0]))

                sleep(waiteTime)
            currentCycle += 1




