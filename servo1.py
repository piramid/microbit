from microbit import *
def servo(pin,degrees):
    degrees=max(0, min(degrees, 180))
    duty= degrees / 180 * 102 + 25
    pin.write_analog(duty)
while 1:
    servo(pin14,0)
    sleep(2000)
    servo(pin14,45)
    sleep(2000)
    servo(pin14,90)
    sleep(2000)
    servo(pin14,135)
    sleep(2000)
    servo(pin14,180)
    sleep(2000)

