import pyautogui
import time

while True:
    w = input('say sth: ')
    if w == 'end':
        break
    time.time(5)
    for i in range(1, 6000):
        pyautogui.typewrite(w)
        pyautogui.press('enter')

