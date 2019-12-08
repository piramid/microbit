from microbit import *
while True:
    button0 = pin0.read_digital()
    button1 = pin1.read_digital()
    if button0==0:
        display.show(Image.YES)
        pin8.write_digital(1)
    if button0==1:
        display.clear()
        pin8.write_digital(0)
    if button1==0:
        display.show(Image.ANGRY)
        pin12.write_digital(1)
    if button1==1&button0==1: #protect blink of Image.YES
        display.clear()
        pin12.write_digital(0)
    sleep(20)
