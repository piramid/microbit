from microbit import *

# charset is a list of ASCII codes in our character set
charset = [i for i in range(65,91)] # upper case letters
charset += [k for k in range(48,58)] # digits
charset += [l for l in range(32,48)] # punctuation and symbols

# chars is a list of characters in our character set
chars = [chr(i) for i in charset]

def GetLetter():
    current = 0
    display.show(chars[current])
    while button_a.was_pressed()==False:
        if accelerometer.get_x()>300:
            current -= 1
            sleep(500)
        elif accelerometer.get_x()<-300:
            current += 1
            sleep(500)
        current = max(0, min(current, len(chars)-1))    
        display.show(chars[current])      
    return chars[current]

def GetString():
    usertext = ""
    while button_b.is_pressed()==False:
        usertext += GetLetter()
    return usertext
    
currentWord = ""

while True:
    while button_a.was_pressed()==False:
        display.scroll(currentWord)
    currentWord = GetString()
