#rust anti-afk mover, by deviousname

import keyboard
import time
import random

keys = ['w','a','s','d']
hotkey = 'shift+del'
stop = 'f9'

class AntiAFK():
    def __init__(self):
        print(f'Adding hotkey: {hotkey} = Toggle Anti AFK')
        keyboard.add_hotkey(f'{hotkey}', lambda: self.toggle_anti_afk())
        print('Ready')
        
    def toggle_anti_afk(self):
        keyboard.unhook_all_hotkeys()
        print(f'Anti AFK has started, press and hold {stop} to stop.')
        while True:
            if keyboard.is_pressed(f'{stop}'):
                print(f'Stopping. Press {hotkey} to start again.')
                keyboard.add_hotkey(f'{hotkey}', lambda: self.toggle_anti_afk())
                break
            key = random.choice(keys)
            keyboard.press_and_release(f'{key}')
            time.sleep(1 + random.random())
                                
initiate = AntiAFK()
