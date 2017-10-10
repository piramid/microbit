from microbit import *
import radio

chnl = 10
radio.config(channel=chnl)
radio.on()

def Drive(lft,rgt):
    pin8.write_digital(0)
    pin12.write_digital(0)
    if lft<0:
        pin8.write_digital(1)
        lft = 1023 + lft
    if rgt<0:
        rgt = 1023 + rgt
        pin12.write_digital(1)
    pin0.write_analog(lft)
    pin1.write_analog(rgt)

while True:
    s = radio.receive()
    if s is not None:
        if s=="N":
            Drive(800,800)
            display.show(Image.ARROW_N)
        elif s=="S":
            Drive(-800,-800)
            display.show(Image.ARROW_S)
        elif s=="NE":
            Drive(800,200)
            display.show(Image.ARROW_NE)
        elif s=="NW":
            Drive(200,800)
            display.show(Image.ARROW_NW)
        elif s=="SE":
            Drive(-800,-200)
            display.show(Image.ARROW_SE)
        elif s== "SW":
            Drive(-200,-800)
            display.show(Image.ARROW_SW)
    else:
        Drive(0,0)
    sleep(20)
