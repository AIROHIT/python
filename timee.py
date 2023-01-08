import pyautogui
import time
time.sleep(4)
count=0
while count<=1000:
    pyautogui.typewrite("i love you"+str(count))
    pyautogui.press("enter")
    count=count+1
    
              
