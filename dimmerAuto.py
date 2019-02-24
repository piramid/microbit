from microbit import *
pin0.write_digital(0)
pin1.write_digital(0)
pin2.write_digital(0)
sleep(1000)

while True:
    for i in range(0, 1024):
        pin0.write_analog(i)
        pin1.write_analog(i)
        pin2.write_analog(i)
        sleep(10)
    for i in range(1023, -1, -1):
        pin0.write_analog(i)
        pin1.write_analog(i)
        pin2.write_analog(i)
        sleep(10)