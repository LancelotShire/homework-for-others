import pyautogui
import time
def click():
    pyautogui.click()
    return 0
for i in range(100):
    click()
    time.sleep(1)

