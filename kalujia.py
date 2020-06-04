import pyautogui
from time import sleep
pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True



baseX,baseY = x,y = pyautogui.center(pyautogui.locateOnScreen('map.png'))

doneX = baseX + 400
doneY = baseY - 139

stopX = baseX + 735
stopY = baseY - 270

packX = baseX + 790
packY = baseY + 30

cureX = baseX + 392
cureY = baseY - 87

sureX = baseX + 365
sureY = baseY - 154

closeX = baseX + 400
closeY = baseY - 367


while True: # 这个小游戏一周只可以玩 10 次？
    # pyautogui.moveTo(300, 300, duration=0.25)
    # x, y = pyautogui.position()
    # print(x,y)
    # pyautogui.click(x, y)
    print('暂停传送带')
    pyautogui.click(stopX, stopY)

    # 点击卡鲁加开始对战
    print('寻找卡鲁加')
    temp = None
    i = 0
    while temp == None: #最多找 1000 次
        temp = pyautogui.locateOnScreen('kalujia.png')
        i += 1
        if (i == 1000):
            break
    x,y = pyautogui.center(temp) 
    pyautogui.click(x, y)

    # 可能会让我点击前后左右的精灵，！！！

    print('等待战斗完成')
    sleep(20) # 4 倍速情况下够用了

    print('确认战斗胜利')
    pyautogui.click(doneX, doneY) # 确认战斗胜利
    sleep(5)
    print('确认 NoNo 的额外经验')
    pyautogui.click(doneX, doneY + 30) # 确认 NoNo 的额外经验

    # 如果升级的话，学习了新的技能还需要特殊处理 ！！！

    sleep(10)
    print('确认掉落的材料')
    pyautogui.click(doneX, doneY) # 确认掉落的材料

    # 治疗精灵
    sleep(5)
    print('治疗精灵')
    pyautogui.click(packX, packY) # 确认掉落的材料
    sleep(5)
    pyautogui.click(cureX, cureY) # 点击治疗
    sleep(5)
    pyautogui.click(sureX, sureY) # 确认治疗
    sleep(5)
    pyautogui.click(closeX, closeY) # 关闭背包



    