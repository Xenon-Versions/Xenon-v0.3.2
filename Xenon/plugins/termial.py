import pyautogui as gui
import mouseinfo
import vars_setup


def step1():
    s1 = gui.locateOnScreen(vars_setup.newPath(vars_setup.change_processPath, "step-1.png"))
    gui.rightClick(s1)
    if not s1:
        s1 = gui.locateOnScreen(vars_setup.newPath(vars_setup.change_processPath, "step-1-2.png"))
        gui.rightClick(s1)


def step2():
    s2 = gui.locateOnScreen(vars_setup.newPath(vars_setup.change_processPath, "step-2.png"))
    gui.click(s2)


def step3():
    s3 = gui.locateOnScreen(vars_setup.newPath(vars_setup.change_processPath, "step-4.png"))
    current_pos = list(mouseinfo.position())
    gui.moveTo(current_pos[0] - 5, current_pos[1])
    current_pos = list(mouseinfo.position())
    gui.moveTo(current_pos[0] + 10, current_pos[1] + 25)
    gui.click()
    gui.press("backspace")
    gui.typewrite("20")


def step4():
    s4 = gui.locateOnScreen(vars_setup.newPath(vars_setup.change_processPath, "step-4.png"))
    gui.click(s4)
    current_pos = list(mouseinfo.position())
    gui.click(current_pos[0] - 5, current_pos[1])
    current_pos = list(mouseinfo.position())
    gui.click(current_pos[0] + 10, current_pos[1] + 25)
    gui.press("backspace")
    gui.typewrite("20")


def step5():
    s5 = gui.locateOnScreen(vars_setup.newPath(vars_setup.change_processPath, "step-5.png"))
    gui.click(s5)


def step6():
    s6 = gui.locateOnScreen(vars_setup.newPath(vars_setup.change_processPath, "step-6.png"))
    gui.moveTo(s6)
    current_pos = list(mouseinfo.position())
    gui.click(current_pos[0] + 160, current_pos[1])


def step7():
    s7 = gui.locateOnScreen(vars_setup.newPath(vars_setup.change_processPath, "step-7.png"))
    gui.click(s7)


def beautify(hi):
    step1()
    step2()
    step3()
    step4()
    step5()
    step6()
    step7()
