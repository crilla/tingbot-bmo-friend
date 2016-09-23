import tingbot
from tingbot import *
import time
import random
from random import randint

options = {'animate' : 0, 'clicked': 0, 'last_face': ''}
faces = ['trans_happy', 'happy1', 'happy2', 'surprise1']

@touch()
def on_touch(xy):
    options['animate'] = 1
    options['clicked'] += 1

@left_button.press
def press():
    options['animate'] = 1
    options['clicked'] += 1

@right_button.press
def press():
    options['animate'] = 1
    options['clicked'] += 1

def wait(duration):
    from tingbot.run_loop import main_run_loop
    import time
    main_run_loop._wait(time.time() + duration)

def trans_happy():
    screen.image('bmo_trans1.png')
    wait(0.03)
    screen.image('bmo_trans2.png')
    wait(0.03)
        
    screen.image('bmo_trans3.png')
    wait(randint(1,2))

    screen.image('bmo_trans2.png')
    wait(0.03)
    screen.image('bmo_trans1.png')
    wait(0.03)
        
    options['animate'] = 0
    options['last_face'] = 'trans_happy'

def loop():
    screen.fill(color=(213,252,228))
    if(options['animate'] == 1):
        trans_happy()
    else:
        screen.image('bmo_normal1.png')

tingbot.run(loop)