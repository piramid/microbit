from microbit import *
pin0.write_digital(1)
pin1.write_digital(1)
pin8.write_digital(1)
sleep(1000)
while True:
    for i in range(0,1024):
        pin0.write_analog(i)
    for i in range(1023,-1,-1):
        pin0.write_analog(i)

