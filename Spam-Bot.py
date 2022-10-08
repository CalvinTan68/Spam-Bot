import pyautogui
import time

msg = input("Input text here : ")
n = input("Repetition (in number) : ")

time.sleep(5)

for i in range(0,int(n)):
  pyautogui.typewrite(msg + '\n')
