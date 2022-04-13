#rust anti-afk mover, by deviousname

import keyboard #install keyboard module instructions and documentation: https://pypi.org/project/keyboard/
import time #default python module (already installed)
import random #default python module (already installed)

keys = ['w','a','s','d'] #add your own random keys here, for example put 'spacebar' in to occasionally jump
hotkey = 'shift+del' #this key or key combination will start the script
stop = 'f9' #this key or key combination will stop the script

class AntiAFK(): #create the class
    def __init__(self): #init the class and add hotkey
        print(f'Adding hotkey: {hotkey} = Toggle Anti AFK')
        keyboard.add_hotkey(f'{hotkey}', lambda: self.toggle_anti_afk())
        print('Ready') 
        
    def toggle_anti_afk(self): #run this when start hotkey is pressed
        keyboard.unhook_all_hotkeys() #removes the start hotkey
        print(f'Anti AFK has started, press and hold {stop} to stop.')
        while True: #infinite loop until stop key is pressed
            if keyboard.is_pressed(f'{stop}'): #this is where the stop hotkey takes effect
                print(f'Stopping. Press {hotkey} to start again.')
                keyboard.add_hotkey(f'{hotkey}', lambda: self.toggle_anti_afk()) #adds the start hotkey back
                break #stops the loop
            key = random.choice(keys) #pick a random key from the keys list
            keyboard.press_and_release(f'{key}') #press the chosen key briefly
            time.sleep(1 + random.random()) #sleep for a random time up between 1 and 2 seconds
                                
initiate = AntiAFK() #starts AntiAFK script
