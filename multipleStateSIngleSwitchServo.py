from microbit import *
import tm1637
def servo(pin,degrees):
    degrees=max(0, min(degrees, 180))
    duty= degrees / 180 * 102 + 25
    pin.write_analog(duty)

tm = tm1637.TM1637(clk=pin15, dio=pin16)
oldSwitchState = 0
newSwitchState1 = 0
newSwitchState2 = 0
newSwitchState3 = 0
state = 0
tm.numbers(0, 0)
while True:
    newSwitchState1 = pin1.read_digital()
    sleep(1)
    newSwitchState2 = pin1.read_digital()
    sleep(1)
    newSwitchState3 = pin1.read_digital()
    # if all 3 values are the same we can continue
    if(newSwitchState1 == newSwitchState2) & (newSwitchState1 == newSwitchState3):
        if(newSwitchState1 != oldSwitchState):
            # has the button switch been closed?
            if(newSwitchState1 == 0):
                # increase the value of state
                state = state+1
                print(state)
                if(state > 4):
                    state = 0
                    tm.numbers(0, 0)
                    pin2.write_digital(0)
                    servo(pin14,0)
                    print(state)
                    # Turn on the next LED
                    # Because the value of
                    # state does not change while we are testing
                    # it we don't need to use else if
                if(state == 1):
                    pin2.write_digital(1)
                    tm.numbers(0, 45)
                    servo(pin14, 45)
                    print(state)
                if(state == 2):
                    pin2.write_digital(0)
                    tm.numbers(0, 90)
                    servo(pin14, 90)
                    print(state)
                if(state == 3):
                    pin2.write_digital(1)
                    tm.numbers(1, 35)
                    servo(pin14, 135)
                    print(state)
                if(state == 4):
                    pin2.write_digital(0)
                    tm.numbers(1, 80)
                    servo(pin14, 180)
                    print(state)
        oldSwitchState = newSwitchState1
