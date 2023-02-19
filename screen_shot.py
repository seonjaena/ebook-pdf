import pyautogui
import time

page_num = int(input("페이지 수를 입력하세요: "))
time.sleep(5)

for i in range(1, page_num + 1):
    pyautogui.screenshot('images/page%#04d.png' % i, region=(530, 5, (1385 - 545), 1055))
    time.sleep(0.3)
    pyautogui.scroll(-1)
    time.sleep(0.3)