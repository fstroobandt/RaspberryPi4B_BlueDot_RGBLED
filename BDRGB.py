from gpiozero import RGBLED
from bluedot import BlueDot
from colorzero import Color

bd=BlueDot(cols=3, rows=4)
led=RGBLED(red=17,green=27,blue=22, active_high=False,pwm=True)

bd[0,0].color="#ff0000" ; bd[1,0].color="#ff7f00" ; bd[2,0].color="#ffff00"

bd[0,1].color="#00ff00" ; bd[1,1].color="#00ff7f" ; bd[2,1].color="#00ffff"

bd[0,2].color="#0000ff" ; bd[1,2].color="#7f00ff" ; bd[2,2].color="#ff00ff"

bd[0,3].visible=False   ; bd[1,3].color="#000000" ; bd[2,3].color="#ffffff"

def red():
    led.color=Color('red')
def orange():
    led.color=Color('orange')
def yellow():
    led.color=Color('yellow')

def green():
    led.color=Color('green')
def turquoise():
    led.color=Color('turquoise')
def cyan():
    led.color=Color('cyan')

def blue():
    led.color=Color('blue')
def purple():
    led.color=Color('purple')
def magenta():
    led.color=Color('magenta')

bd[0,0].when_pressed=red
bd[1,0].when_pressed=orange
bd[2,0].when_pressed=yellow

bd[0,1].when_pressed=green
bd[1,1].when_pressed=turquoise
bd[2,1].when_pressed=cyan

bd[0,2].when_pressed=blue
bd[1,2].when_pressed=purple
bd[2,2].when_pressed=magenta

bd[1,3].when_pressed=led.off
bd[2,3].when_pressed=led.on

while(True):
    bd.wait_for_press()
