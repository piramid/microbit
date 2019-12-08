from microbit import *
import tm1637
tm=tm1637.TM1637(clk=pin15,dio=pin16)
while 1:
    tm.show('{:04d}'.format(pin2.read_analog()))
    sleep(100)
