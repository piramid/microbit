from microbit import *
compass.calibrate()
while True:
    bearing = compass.heading()
    print("bearing : " , bearing)
    x = compass.get_x()
    y = compass.get_y()
    z = compass.get_z()
    print("x: " + str(x) + " y: " + str(y) + " z: " + str(z))
    sleep(100)
