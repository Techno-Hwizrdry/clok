__author__  = "Alexan Mardigian"
__version__ = "1.0.0"

import time
import tingbot

from tingbot import *

state = {'is_pressed': False}

@right_button.press
def press():
    s = state['is_pressed']
    
    if s:
        s = False
    else:
        s = True

    state['is_pressed'] = s
    
@touch()
def on_touch(xy, action):
    if action == 'down':
        press()

@every(seconds=1.0/30)
def loop():
    date_format_str = "%d %B %Y"
    time_format_str = "%H:%M:%S"
    
    if state['is_pressed']:
        time_format_str = "%I:%M:%S %p"
    
    current_date = time.strftime("%d %B %Y")
    current_time = time.strftime(time_format_str)
    
    screen.fill(color='blue')
    
    screen.text(current_time, xy=(160, 110), color='white', font_size=50)
    screen.text(current_date, xy=(160, 180), color='grey', font_size=24)

tingbot.run()
