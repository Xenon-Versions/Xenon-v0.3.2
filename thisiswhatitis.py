import pyautogui as gui
import mouseinfo

s1 = gui.locateOnScreen("C:/Users/Acer/Desktop/change-process/step-1.png")
gui.rightClick(s1)
if not s1:
    s1 = gui.locateOnScreen("C:/Users/Acer/Desktop/change-process/step-1-2.png")
    gui.rightClick(s1)

s2 = gui.locateOnScreen("C:/Users/Acer/Desktop/change-process/step-2.png")
gui.click(s2)
s3 = gui.locateOnScreen("C:/Users/Acer/Desktop/change-process/step-3.png")
gui.click(s2)
current_pos = list(mouseinfo.position())
gui.moveTo(current_pos[0]+10,current_pos[1]+25)
gui.click()
gui.press("backspace")
gui.press("backspace")
gui.press("backspace")
gui.typewrite("20")
s4 = gui.locateOnScreen("C:/Users/Acer/Desktop/change-process/step-4.png")
gui.click(s4)
s5 = gui.locateOnScreen("C:/Users/Acer/Desktop/change-process/step-5.png")
gui.click(s5)
s6 = gui.locateOnScreen("C:/Users/Acer/Desktop/change-process/step-6.png")
gui.moveTo(s6)
current_pos = list(mouseinfo.position())
gui.click(current_pos[0]+160,current_pos[1])
s7 = gui.locateOnScreen("C:/Users/Acer/Desktop/change-process/step-7.png")
gui.click(s7)