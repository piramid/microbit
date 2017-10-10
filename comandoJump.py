from microbit import *


def startGame():
    countDown()
    drawPlayArea()


def flashMan(x, y, p, vx, vy):
    display.set_pixel(x, y, 0)
    display.set_pixel(x+vx, y+vy, 0)
    sleep(100)
    display.set_pixel(x, y, 9-p)
    display.set_pixel(x+vx, y+vy, p)
    sleep(100)


def moveHorizontal():
    for x in range(4, 0, -1):
        for fraction in range(0, 10):
            flashMan(x, 0, fraction, -1, 0)


def moveVertical(x, h):
    if h != 0:
        display.set_pixel(x, h-1, 0)
        for y in range(h, 4):
            for fraction in range(0, 10):
                flashMan(x, y, fraction, 0, 1)


def playGame():
    position = 4
    button_a.reset_presses()
    t1 = running_time()
    press = 0
    while(running_time()-t1 < 20000):
        flashMan(4, position, press, 0, -1)
        press = button_a.get_presses()
        if press >= 10:
            position = position-1
            button_a.reset_presses()
            press = 0
            if position == 0:
                break
    return position


def endGame(position):
    if position == 0:
        moveHorizontal()
        moveVertical(0, 0)
    else:
        moveVertical(4, position)


def countDown():
    for t in range(5, 0, -1):
        display.scroll(str(t))
        display.scroll("!")


def drawPlayArea():
    display.clear()
    for y in range(1, 5):
        display.set_pixel(2, y, 9)


startGame()
position = playGame()
endGame(position)
