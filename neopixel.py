from microbit import *
import neopixel
from random import randint

# Setup the Neopixel strip on pin14 with a length of 12 pixels
np = neopixel.NeoPixel(pin14, 12)

while True:
    #Iterate over each LED in the strip

    for pixel_id in range(0, len(np)):
        red = randint(0, 10)
        green = randint(0, 10)
        blue = randint(0, 10)
        print(np)

        # Assign the current LED a random red, green and blue value between 0 and 60
        np[pixel_id] = (red, green, blue)

        # Display the current pixel data on the Neopixel strip
        np.show()
        sleep(100)
