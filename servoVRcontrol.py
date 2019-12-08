from microbit import *
def servo(pin,degrees):
    degrees=max(0, min(degrees, 180))
    duty= degrees / 180 * 102 + 25
    pin.write_analog(duty)
while 1:
    VR=int(pin2.read_analog()*180/1023)
    print(VR)
    servo(pin14,VR)
    sleep(100)
