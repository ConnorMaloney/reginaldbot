# Import modules
import pyautogui, time, sys

# Handle emergency termination
pyautogui.PAUSE = 0.1
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
        # Clicks smelter coordinates
        pyautogui.click(892,48) 
        for i in range(20,0,-1):
            #sys.stdout.write(str(i)+' ')
            #sys.stdout.flush()
            #time.sleep(1)
            numStr = "Walking to smelter: " + str(i).rjust(4)
            print(numStr, end='')
            print('\b' * len(numStr), end='', flush=True)
            time.sleep(1)
        print("\n")

        # Clicks bank coordinates
        pyautogui.click(856,186)
        for i in range(20,0,-1):
            #sys.stdout.write(str(i)+' ')
            #sys.stdout.flush()
            #time.sleep(1)
            numStr = "Walking to bank: " + str(i).rjust(4)
            print(numStr, end='')
            print('\b' * len(numStr), end='', flush=True)
            time.sleep(1)
        print("\n")
except KeyboardInterrupt:
    print('\nAbort.')