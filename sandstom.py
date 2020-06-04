import pyautogui
from time import sleep
pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True


for i in range(0,10): # 这个小游戏一周只可以玩 10 次？
    # pyautogui.moveTo(300, 300, duration=0.25)
    # x, y = pyautogui.position()
    # print(x,y)
    # pyautogui.click(x, y)
    
    # 点击大树进入游戏
    x,y = pyautogui.center(pyautogui.locateOnScreen('gameGate.png')) 
    pyautogui.click(x, y)
    pyautogui.moveTo(1, 1, duration=0.25) # 把鼠标移动到界面外，因为赛尔号图标是会有鼠标漂浮的响应

    # 点击开始，开始游戏
    x,y = pyautogui.center(pyautogui.locateOnScreen('start.png')) 
    pyautogui.click(x, y)
    pyautogui.moveTo(1, 1, duration=0.25) # 把鼠标移动到界面外，因为赛尔号图标是会有鼠标漂浮的响应
    # 点击三次继续，到第四关
    temp = None
    while temp == None:
        temp = pyautogui.locateOnScreen('continue.png')
    x,y = pyautogui.center(temp) 
    pyautogui.click(x, y)
    pyautogui.moveTo(1, 1, duration=0.25) # 把鼠标移动到界面外，因为赛尔号图标是会有鼠标漂浮的响应

    sleep(10)
    pyautogui.click(x, y)
    pyautogui.moveTo(1, 1, duration=0.25) # 把鼠标移动到界面外，因为赛尔号图标是会有鼠标漂浮的响应
    sleep(10)
    pyautogui.click(x, y)
    pyautogui.moveTo(1, 1, duration=0.25) # 把鼠标移动到界面外，因为赛尔号图标是会有鼠标漂浮的响应

    # 点击选项，退出游戏
    x,y = pyautogui.center(pyautogui.locateOnScreen('optinos.png')) 
    pyautogui.click(x, y)
    pyautogui.moveTo(1, 1, duration=0.25) # 把鼠标移动到界面外，因为赛尔号图标是会有鼠标漂浮的响应

    x,y = pyautogui.center(pyautogui.locateOnScreen('quit.png')) 
    pyautogui.click(x, y)
    pyautogui.moveTo(1, 1, duration=0.25) # 把鼠标移动到界面外，因为赛尔号图标是会有鼠标漂浮的响应
    # 点击确认
    sleep(5) # 延迟一下
    x,y = pyautogui.center(pyautogui.locateOnScreen('done.png')) 
    pyautogui.click(x, y)
    pyautogui.moveTo(1, 1, duration=0.25) # 把鼠标移动到界面外，因为赛尔号图标是会有鼠标漂浮的响应

    