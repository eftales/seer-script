# 参考 https://blog.csdn.net/longgb123/article/details/79090559
# 需要管理员权限，不要再运行脚本的 cmd 框里面点击，会很卡！！！直接点击赛尔号就行！！
from pynput.mouse import Listener,Button

events = []
base = [-1,-1]



def on_click(x, y, button, pressed):
    if pressed:
        # 监听鼠标点击
        if button == Button.left:
            print(x,y)
            if base[0] == -1 or base[1] == -1:
                base[0] = x
                base[1] = y
                
            else:
                events.append((x-base[0],y-base[1]))
        else :
            with open('sequence.txt','w') as f:
                for each in events:
                    f.write( "\n" + str(each[0]) + "\t" + str(each[1]) + "\t" )

            print("点击序列已经写入了 sequence.txt，你还需要在 sequence.txt 的第一行写上运行参数")
            return False




# 连接事件以及释放
with Listener(on_click=on_click) as listener:
    listener.join()
# 一个鼠标监听器是一个线程。线程，所有的回调将从线程调用。从任何地方调用pynput.mouse.Listener.stop，或者调用pynput.mouse.Listener.StopException或从回调中返回False来停止监听器。