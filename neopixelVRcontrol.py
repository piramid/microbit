from microbit import *
import neopixel
import tm1637
tm=tm1637.TM1637(clk=pin15,dio=pin16)
np = neopixel.NeoPixel(pin14, 16)
while True:
    x=pin1.read_analog()
    y=int(x/4)
    tm.show('{:04d}'.format(pin1.read_analog()))
    if(x>512):
        for i in range(0,12):
            np[i] = (0,y,0)
        np.show()
    else:
        for i in range(0,12):
            np[i] = (0,0,y)
        np.show()

