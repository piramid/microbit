from microbit import *
pin0.write_digital(1)
pin1.write_digital(1)
pin8.write_digital(1)
sleep(1000)
while True:
    pin0.write_digital(0)
    sleep(1000)
    pin0.write_digital(1)
    pin1.write_digital(0)
    sleep(1000)
    pin1.write_digital(1)
    pin8.write_digital(0)
    sleep(1000)
    pin8.write_digital(1)



