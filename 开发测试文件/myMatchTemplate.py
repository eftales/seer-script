import cv2
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
# 483 574
# 476 27 
baseX = 1414
baseY = 801
img = pyautogui.screenshot(region=(baseX - 483,baseY - 574, baseX + 476,baseY + 27)) # x,y,w,h
img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
template = cv2.imread('pipi.png',0)
w, h = template.shape[::-1]
template = cv2.cvtColor(np.asarray(template),cv2.COLOR_RGB2BGR)

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

meth = methods[1]

method = eval(meth)

# Apply template Matching
res = cv2.matchTemplate(img,template,method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img,top_left, bottom_right, (255,0,0) , 2)

print(top_left, bottom_right)

plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle(meth)

plt.show()
