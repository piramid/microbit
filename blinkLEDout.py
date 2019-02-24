from microbit import *
pin0.write_digital(0)
pin1.write_digital(0)
pin2.write_digital(0)
sleep(1000)

while True:
    for i in range(0, 1024):
        pin0.write_analog(i)
