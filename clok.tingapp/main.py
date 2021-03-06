__author__  = "Alexan Mardigian"
__version__ = "1.0.0"

import os
import time
import tingbot

from tingbot import *

SAVEFILE = 'saved_font.sav'

def load_fonts():
    x = 0
    f = {}

    path  = "./fonts/"
    files = os.listdir(path)
    
    for filename in files:
        if filename.endswith(".ttf"):
            f.update( {x: path + filename} )
            x += 1
        
    return f

fonts = load_fonts()
state = { 'is_fomrat_pressed': False,
          'selected_font': 0
}

def get_saved_font():
    infile = open(SAVEFILE, 'a+')
    
    try:
        font_path = infile.readlines()[0]
    except IndexError:
        font_path = ''

    infile.close()
    
    return font_path

@left_button.press
def cycle_font():
    state['selected_font'] += 1
    
    # Check if we have reached the end of the list.
    # If we have, then go back to the beginning of the list. 
    
    if state['selected_font'] >= len(fonts):
        state['selected_font'] = 0
    
    outfile = open(SAVEFILE, 'w')
    outfile.write(fonts[state['selected_font']])
    outfile.close()

@right_button.press
def set_time_format():
    s = state['is_fomrat_pressed']
    
    if s:
        s = False
    else:
        s = True

    state['is_fomrat_pressed'] = s
    
@touch()
def on_touch(xy, action):
    if action == 'down':
        set_time_format()

@every(seconds=1.0/30)
def loop():
    date_format_str = "%d %B %Y"
    time_format_str = "%H:%M:%S"
    
    sf = get_saved_font()
    
    if not sf:
        sf = fonts[state['selected_font']]
    
    if state['is_fomrat_pressed']:
        time_format_str = "%I:%M:%S %p"
    
    current_date = time.strftime("%d %B %Y")
    current_time = time.strftime(time_format_str)
    
    screen.fill(color='black')
    
    screen.text(current_time, xy=(160, 110), color='yellow', font_size=47, font=sf)
    screen.text(current_date, xy=(160, 180), color='yellow', font_size=24, font=sf)

tingbot.run()
