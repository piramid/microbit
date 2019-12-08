from microbit import *
import tm1637

tm = tm1637.TM1637(clk=pin15, dio=pin16)
oldSwitchState = 0
newSwitchState1 = 0
newSwitchState2 = 0
newSwitchState3 = 0
state = 0
tm.numbers(0, 0)
while True:
    newSwitchState1 = pin0.read_digital()
    sleep(1)
    newSwitchState2 = pin0.read_digital()
    sleep(1)
    newSwitchState3 = pin0.read_digital()
    # if all 3 values are the same we can continue
    if(newSwitchState1 == newSwitchState2) & (newSwitchState1 == newSwitchState3):
        if(newSwitchState1 != oldSwitchState):
            # has the button switch been closed?
            if(newSwitchState1 == 0):
                # increase the value of state
                state = state+1
                print(state)
                if(state > 3):
                    state = 0
                    tm.numbers(0, 0)
                    pin2.write_digital(0)
                    print(state)
                    # Turn on the next LED
                    # Because the value of
                    # state does not change while we are testing
                    # it we don't need to use else if
                if(state == 1):
                    pin2.write_digital(1)
                    tm.numbers(1, 1)
                    print(state)
                if(state == 2):
                    pin2.write_digital(0)
                    tm.numbers(2, 2)
                    print(state)
                if(state == 3):
                    pin2.write_digital(1)
                    tm.numbers(3, 3)
                    print(state)
        oldSwitchState = newSwitchState1
