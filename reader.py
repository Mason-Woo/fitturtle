from evdev import uinput, ecodes as e
import time
import sys


def hit_key(k):
    print('p:',k)
    ui.write(e.EV_KEY, k, 1)
    ui.write(e.EV_KEY, k, 0)
    ui.syn()

class State:
    LEFT = 0
    RIGHT = 1
    STOP = 2

with uinput.UInput() as ui:
    state = State.STOP
    while True:   
        f = open(sys.argv[1],'r')
        s = f.read()
        print('d:',s)
        print('s:',state)
        if s[0] == '0':       
            if state == State.RIGHT:
                hit_key(e.KEY_LEFT)
                hit_key(e.KEY_LEFT)
            elif state == State.LEFT:
                hit_key(e.KEY_RIGHT)
                hit_key(e.KEY_RIGHT)
            else:
                assert(state == State.STOP)
            state = State.STOP
        elif s[0] == '1':
            if state == State.STOP:
                hit_key(e.KEY_LEFT)
                hit_key(e.KEY_LEFT)
            elif state == State.RIGHT:
                hit_key(e.KEY_LEFT)
                hit_key(e.KEY_LEFT)
                hit_key(e.KEY_LEFT)
                hit_key(e.KEY_LEFT)
            else:
                assert(state == State.LEFT)
            state = State.LEFT
        elif s[:2] == '-1':
            if state == State.STOP:
                hit_key(e.KEY_RIGHT)
                hit_key(e.KEY_RIGHT)
                state = State.RIGHT
            elif state == State.LEFT:
                hit_key(e.KEY_RIGHT)
                hit_key(e.KEY_RIGHT)
                hit_key(e.KEY_RIGHT)
                hit_key(e.KEY_RIGHT)
            else:
                assert(state == State.RIGHT)
            state = State.RIGHT	
        else:
            assert(False and "Error !!!")
        
        time.sleep(0.1)
