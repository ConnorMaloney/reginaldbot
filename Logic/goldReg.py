# Import modules
import pyautogui, time, sys

# Important coordinates
#
# BANK - Can differ by 5 pixels
# ~(260, 490) - Position of banker
# ~(230, 100) - Position of bank tab 1 (where gold and necklaces are)
# ~(200, 140) - Position of gold bars in bank inv
# ~(245, 145) - Position of gold necklaces in bank inv
#
# SMELTER - Can differ by 5 pixels
# ~(300, 450) - Position of Smelter (Can actually differ by 50 pixels)
# ~(220, 450) - Position of "Make 1 gold necklace"
# ~(195, 535) - Position of "Make All gold necklace" after right click (Right click coords causes menu to vary position)
#
# MAP COORDS - Can differ by 3 pixels
# ~(890, 50) - Position of Al Kharid smelter (from first Northward bank teller)
# ~(850, 185) - Position of Al Kharid bank (from smelter)
# 
# BUTTON COORDS - Can differ by 10 pixels
# ~(645, 1015) - Position of inventory button

# Important Notes: Takes ~53 seconds to smelt 23 gold necklaces. Crafting levelup can popup at anytime
# and interrupt this process. Press spacebar 3-5 times to skip over this.

# Handle emergency termination
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# Testing loop dragging functions for combining ingredients
print('Crafting gold amulets. Press Ctrl-C to quit.')
print("Starting bot in...\n")
for i in range(5,0,-1):
    print(i, end='')
    print('\b' * len(str(i)), end='', flush=True)
    time.sleep(1)

#x, y = pyautogui.position()
 #       positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
  #      print(positionStr, end='')
   #     print('\b' * len(positionStr), end='', flush=True)

pyautogui.click() # Click brings in focus (have this on osrs window)

try: 
    while True:
        print("Starting with empty inventory. Loading up on gold...\n")
        pyautogui.click(645, 1015) # clicks inventory button
        pyautogui.click(260, 490) # clicks banker
        pyautogui.click(230, 100) # clicks bank tab 1
        pyautogui.click(200, 140) # clicks gold bars
        pyautogui.click(892, 48) # clicks smelter coords
        for i in range(20,0,-1):
            numStr = "Walking to smelter: " + str(i).rjust(4)
            print(numStr, end='')
            print('\b' * len(numStr), end='', flush=True)
            time.sleep(1)
        print("\n")
        print("At smelter, cooking")

        # Clicks bank coordinates
        pyautogui.click(856,186)
        for i in range(20,0,-1):
            numStr = "Walking to bank: " + str(i).rjust(4)
            print(numStr, end='')
            print('\b' * len(numStr), end='', flush=True)
            time.sleep(1)
        print("\n")
except KeyboardInterrupt:
    print('\nAbort.')