from microbit import *
while True:
    if accelerometer.is_gesture("up"):
        display.show(Image.ARROW_N)
    elif accelerometer.is_gesture("right"):
        display.show(Image.ARROW_E)
    elif accelerometer.is_gesture("down"):
        display.show(Image.DIAMOND)
    elif accelerometer.is_gesture("left"):
        display.show(Image.ARROW_W)
    elif accelerometer.is_gesture("shake"):
        display.show(Image.HAPPY)
    elif accelerometer.is_gesture("face up"):
        display.show(Image.BUTTERFLY)
    elif accelerometer.is_gesture("face down"):
        display.show(Image.CHESSBOARD)
    else:
        display.clear()
    sleep(20)
