from microbit import *
import tm1637
tm=tm1637.TM1637(clk=pin15,dio=pin16)
Sec=0
Min=0
while 1:
    if (Sec<59):
        Sec=Sec+1
    else:
        Sec=0
        Min=Min+1
    tm.numbers(Min,Sec)
    sleep(1000)
