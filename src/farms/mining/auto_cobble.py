import minescript as m
import time

'''
    @author fl3shware
    @description Quad-directional cobblestone farm 
'''

def auto_mining():
    time.sleep(.05)
    m.player_press_attack(True)
    time.sleep(.95)
    m.player_press_attack(False)
    time.sleep(.5)

def anti_afk():
    m.player_press_left(True)
    time.sleep(.1)
    m.player_press_left(False)
    time.sleep(.1)
    m.player_press_right(True)
    time.sleep(.1)
    m.player_press_right(False)
    time.sleep(.1)

def main():
    while True:
        p_or = m.player_orientation()
        m.player_set_orientation(p_or, 0)
        auto_mining()

        m.player_set_orientation(p_or + 90, 0)
        auto_mining()

        m.player_set_orientation(p_or - 90, 0)
        auto_mining()

        m.player_set_orientation(p_or + 180, 0)
        auto_mining()

        m.player_set_orientation(p_or, 0)
        anti_afk()

if __name__ == "__main__":
    main()
