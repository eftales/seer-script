# 简介
为了减轻赛尔号的肝度，特意设计了该脚本。。。（没想到过了这么多年，赛尔号还是这么肝）
## 依赖
python3+
pyautogui
pynput

# 软件思路
本软件基于操作序列，runSequence.py 读取同级目录下的 sequence.txt 文件,将其解析为操作序列,然后顺次执行该序列。

与简单的鼠标录制不同,本软件还支持基于匹配的图像识别,这样就可以自动刷精灵了。

# sequence.txt 格式
第一行代表软件参数，除了第一行，每一行代表一个操作，不同的列有不同的意义，列于列之间用 tab 键（\t） 隔开

x y 坐标全部是相对坐标，原点是星际地图那个同心圆的圆心。

![原点](原点.png)

如果坐标是动态变化的，比如说精灵，那就把精灵的代号写到 x 坐标那个位置，y 坐标空着，直接写说明。

## 第一行
| 操作间隔（单位：秒）  | 循环次数 | 寻找操作最大尝试次数 |
| ----  | ----  | ----  | ----  |
| 8 | 10 | 1000 |

循环次数 = -1 表示一致循环

##  其余行
| x 坐标  | y 坐标 | 说明  |
|  ----  | ----  | ----  |
| 101  | 202 | 确认战斗结束 |
| pipi  |  寻找皮皮 |  |
| 101  | 502 | 使用第一个技能 |

# 辅助工具
mouseRecorder.py 就是鼠标录制工具。

使用方法很简单，开启脚本之后，他会把你第一次左键点击的地方作为原点，依次记录之后每次左键点击的相对坐标，并将这些动作输出为 sequence.txt。

右键点击任何位置退出。

## 注意
1. 使用管理员权限运行该脚本
2. 直接点击赛尔号界面

# 操作演示


# TODO
1. 直接录制鼠标操作可能会好一点，如果操作时间的间隔是确定的，就可能会有各种时序 bug；
2. 怀旧服有选择前后左右防止脚本的操作，选一下；
3. 精灵顺序很重要，需要开发一个自动整理精灵背包的脚本；
4. 不同 sequence 需要的精灵不一样


