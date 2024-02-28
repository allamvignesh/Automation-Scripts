# https://www.silvergames.com/en/piano-tiles

import pyautogui
import time
import keyboard

time.sleep(3)
print("Starting....")

EXIT = False
while not EXIT:

    s = pyautogui.screenshot()
    if s.getpixel((70, 666)) in [(16, 20, 19), (0, 0, 0)]:
        pyautogui.click((70, 666))
        print("1")
    elif s.getpixel((170, 666)) in [(16, 20, 19), (0, 0, 0)]:
        pyautogui.click((170, 666))
        print("2")
    elif s.getpixel((270, 666)) in [(16, 20, 19), (0, 0, 0)]:
        pyautogui.click((270, 666))
        print("3")
    elif s.getpixel((370, 666)) in [(16, 20, 19), (0, 0, 0)]:
        pyautogui.click((370, 666))
        print("4")

    if keyboard.is_pressed("q"):
        EXIT = not EXIT

print("Stopping...")
