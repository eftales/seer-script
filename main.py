import pyautogui
from time import sleep
pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True



baseX,baseY = x,y = pyautogui.center(pyautogui.locateOnScreen('base.png'))



while True: # 这个小游戏一周只可以玩 10 次？
    # pyautogui.moveTo(300, 300, duration=0.25)
    # x, y = pyautogui.position()
    # print(x,y)
    # pyautogui.click(x, y)
    
    # 点击仙人掌开始对战
    print('寻找仙人掌')
    temp = None
    i = 0
    while temp == None: #最多找 1000 次
        temp = pyautogui.locateOnScreen('xianrenzhang1.png')
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
    pyautogui.click(doneX, doneY - 30) # 确认掉落的材料



    