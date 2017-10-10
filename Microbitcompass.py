from microbit import *


# Start calibrating
compass.calibrate()

# Try to keep the needle pointed in (roughly) the correct direction
while True:
    sleep(100)
    b = compass.heading()
    needle = ((12 - compass.heading()) // 30) % 12
    print("needle: " , needle)
    print("bearing: " , b)
    display.show(Image.ALL_CLOCKS[needle])
