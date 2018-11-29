# Import modules
import pyautogui, time, sys

# NOTE: Update 11/20/2018: This method isn't nearly as profitable anymore, will have to find new methods.

#Blackjack bot? jemar10xford, maybe next project

# Important Notes: Takes ~53 seconds to smelt 23 gold necklaces. Crafting levelup can popup at anytime
# and interrupt this process. Press spacebar 3-5 times to skip over this.

# Other bots? Progpmaker and Hoontar00
# Handle emergency termination
pyautogui.PAUSE = 1.3
pyautogui.FAILSAFE = True

# Testing loop dragging functions for combining ingredients
print('Crafting gold amulets. Press Ctrl-C to quit.')
print("Starting reginald in...\n")
for i in range(5,0,-1):
    print(i, end='')
    print('\b' * len(str(i)), end='', flush=True)
    time.sleep(1)
pyautogui.click(645, 1015) # clicks inventory button

# Orients camera north
print("Orienting...\n")
pyautogui.click(1756, 54)
# pyautogui.scroll(-100) # Ensure that game is scrolled out as far as possible
pyautogui.keyDown('up')
pyautogui.keyUp('up')


try: 
    while True:
        # Phase 1: Load inventory with gold bars
        print("Phase 1: Loading/Depositing gold...\n")
        pyautogui.moveTo(265, 485) # Hover over banker to give option
        pyautogui.click(265, 485) # clicks banker
        pyautogui.click(230, 100) # clicks bank tab 1
        pyautogui.click(835, 750) # Clicks first gold amulet (ensure deposit all is on)
        pyautogui.click(200, 140) # clicks gold bars

        # Phase 2: Walk to smelter
        pyautogui.click(890, 50) # clicks smelter coords
        for i in range(20,0,-1):
            numStr = "Phase 2: Walking to smelter... " + str(i).rjust(4)
            print(numStr, end='')
            print('\b' * len(numStr), end='', flush=True)
            time.sleep(1)
        print("\n")

        # Phase 3: Prepare gold bars
        print("Phase 3: Preparing gold...\n")
        pyautogui.moveTo(300, 450) # hovers over smelter to bring option
        pyautogui.click(300, 450) # clicks smelter furnace
        pyautogui.rightClick(220, 450) # right click gold amulet
        pyautogui.click(195, 535) # click Make all gold necklaces

        # Phase 4: Smelt gold bars into gold amulets
        for i in range(53,0,-1):
            numStr = "Phase 4: Smelting gold amulets... " + str(i).rjust(4)
            print(numStr, end='')
            print('\b' * len(numStr), end='', flush=True)
            time.sleep(1)
        print("\n")     
        print("Phase 4.1: Skipping over level up popups...\n")
        pyautogui.press('space')
        pyautogui.press('space')
        pyautogui.press('space')

        print("Phase 4.2: Reinitating smelting process...\n")
        pyautogui.moveTo(300, 450) # hovers over smelter to bring option
        pyautogui.click(300, 450) # clicks smelter furnace
        pyautogui.rightClick(220, 450) # right click gold amulet
        pyautogui.click(195, 535) # click Make all gold necklaces
        for i in range(20,0,-1):
            numStr = "Phase 4.3: Contiuing smelting process... " + str(i).rjust(4)
            print(numStr, end='')
            print('\b' * len(numStr), end='', flush=True)
            time.sleep(1)

        # Phase 5: Walk to bank
        pyautogui.click(855,185) # clicks bank coords
        for i in range(20,0,-1):
            numStr = "Phase 5: Walking back to bank... " + str(i).rjust(4)
            print(numStr, end='')
            print('\b' * len(numStr), end='', flush=True)
            time.sleep(1)
        print("\n")

        # Restart loop
        print("Restarting reginald...\n")
except KeyboardInterrupt:
    print('\nAbort.')