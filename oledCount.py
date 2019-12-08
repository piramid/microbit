from microbit import sleep
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text
initialize()
clear_oled()
x=20
st='cnt='
while 1:
    y=st+str(x)
    add_text(0,2,y)
    x=x-1
    sleep(20)

