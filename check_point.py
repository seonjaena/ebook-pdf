import time
import pyautogui

while True:
    time.sleep(1)
    print( "Current Mouse Position : ", pyautogui.position() )