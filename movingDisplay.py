from microbit import *
im = Image('00000:00000:00900:00000:00000:')
display.show(im)
sleep(500)
while True:
    im = im.shift_up(1)
    display.show(im)
    sleep(500)
    im = im.shift_right(1)
    display.show(im)
    sleep(500)
    im = im.shift_down(1)
    display.show(im)
    sleep(500)
    im = im.shift_left(1)
    display.show(im)
    sleep(500)