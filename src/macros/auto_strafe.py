import minescript as m
import time

'''
    @author fl3shware
    @description Automatic strafing 
'''

def press(key_fn, duration):
    key_fn(True)
    time.sleep(duration)
    key_fn(False)
    time.sleep(0.1)

PATTERN = [
    (m.player_press_left,         3),
    (m.player_press_backward,   0.2),
    (m.player_press_right,        3),
    (m.player_press_forward,    0.2),
        ] 

def auto_strafe():
    while True:
        for action, duration in PATTERN:
            press(action, duration)

if __name__ == "__main__":
    auto_strafe()
