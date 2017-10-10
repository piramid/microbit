from microbit import *
import radio

chnl = 10
radio.config(channel=chnl)
radio.on()


while True:
    y = accelerometer.get_y()
    a = button_a.is_pressed()
    b = button_b.is_pressed()
    if  a and y<-300:
        # forwards left
        display.show(Image.ARROW_NW)
        radio.send("NW")
    elif a and y>300:
        # backwards left
        display.show(Image.ARROW_SW)
        radio.send("SW")
    elif b and y<-300:
        # forwards right
        display.show(Image.ARROW_NE)
        radio.send("NE")
    elif b and y>300:
        # backwards right
        display.show(Image.ARROW_SE)
        radio.send("SE")
    elif y>300:
        #backwards
        display.show(Image.ARROW_S)
        radio.send("S")
    elif y<-300:
        # forwards
        display.show(Image.ARROW_N)
        radio.send("N")
    sleep(20)
