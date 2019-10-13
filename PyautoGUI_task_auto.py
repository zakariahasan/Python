import datetime, pause, pyautogui,time

pause.until(datetime.datetime(2019,7,9,18,3,0))   #pause untill a specific time pause:3d party library

time.sleep(5)
#pyautogui.PAUSE=10

pyautogui.click(1803,13,clicks=1,interval=0.5)
time.sleep ( 2 )

pyautogui.click(217,1064)
time.sleep(2)

pyautogui.click(1270,276,clicks=2)
time.sleep(2)

pyautogui.click(217,184,clicks=2)
time.sleep(2)

pyautogui.click(1855,369,clicks=2)
time.sleep(2)
