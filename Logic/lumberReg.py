# Import modules
import pyautogui, time, sys

# Woodcutting bot at Varrock, near Bank of Gielinor

# Important coordinates
# COMPASS - Can differ by 8 pixels
# ~(797, 56) - Position of orientation button 
# 
# BANK - Can differ by 2 pixels
# ~(912, 235) - Position of "Bank bank booth" (closest to south door, from facing oak tree)
# ~(230, 100) - Position of bank tab 1 (where oak logs are)
# ~(245, 145) - Position of logs in bank inv
# ~(600, 68) - Position of close button
#
# TREE - Can differ by 2 pixels
# ~(436, 113) - Position of "Chop down oak" from bank booth, after orientation
# ~(519, 495) - Position of stump from left side
# ~(395, 120) - Potential position of tree (POSSIBLE)
# 
# INVENTORY - Can differ by 10 pixels
# ~(645, 1015) - Position of inventory button
# ~(915, 970) - Position of last inventory item (should be last oak log)
#
# Important Notes: Takes ~53 seconds to smelt 23 gold necklaces. Crafting levelup can popup at anytime
# and interrupt this process. Press spacebar 3-5 times to skip over this.
#
# Other bots? Progpmaker and Hoontar00
#
# 1.3 seconds after each command, DO NOT CHANGE, WILL AFFECT CAMERA ORIENTATION
pyautogui.PAUSE = 1.3
# Handle emergency termination (move mouse to upper left of screen)
pyautogui.FAILSAFE = True

print('Cutting oak logs. Press Ctrl-C to quit.')
print("Starting reginald in...\n")
for i in range(5,0,-1):
    print(i, end='')
    print('\b' * len(str(i)), end='', flush=True)
    time.sleep(1)

# Orients camera north
pyautogui.click(797, 56)
#pyautogui.scroll(-100) # Ensure that game is scrolled out as far as possible
pyautogui.keyDown('up')
pyautogui.keyUp('up')

try:
    pyautogui.keyDown('right')
    pyautogui.keyUp('right')
 #   for i in range(3,0,-1): 
        # Testing
  #      pyautogui.keyDown('right')
   #     pyautogui.keyUp('right')
    #    pyautogui.keyDown('left')
     #   pyautogui.keyUp('left')

except KeyboardInterrupt:
    print('\nAbort.')