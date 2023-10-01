import pyautogui
import math
import time

increments = 200
radius = 400

time.sleep(3)

pyautogui.PAUSE = 0.01

offset = (960, 520)

pyautogui.moveTo(offset[0] + radius, offset[1])

pyautogui.mouseDown()

for i in range(increments):
    theta = math.pi * 2 / increments * i
    x = math.cos(theta) * radius
    y = math.sin(theta) * radius
    pyautogui.moveTo(x + offset[0], y + offset[1])
pyautogui.mouseUp()