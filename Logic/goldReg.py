# Import modules
import pyautogui, time, sys

# Handle emergency termination
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

# Testing loop dragging functions for combining ingredients
print('Crafting gold amulets. Press Ctrl-C to quit.')
print("Starting bot in...\n")
for i in range(5,0,-1):
    sys.stdout.write(str(i)+' ')
    sys.stdout.flush()
    time.sleep(1)

pyautogui.click() # Click brings in focus (have this on osrs window)

try: 
    while True:
        pyautogui.click(892,48)
        print("Walking to smelter...\n")
        for i in range(20,0,-1):
            sys.stdout.write(str(i)+' ')
            sys.stdout.flush()
            time.sleep(1)
        pyautogui.click(856,186)
        print("Walking to bank...\n")
        for i in range(20,0,-1):
            sys.stdout.write(str(i)+' ')
            sys.stdout.flush()
            time.sleep(1)
except KeyboardInterrupt:
    print('\nAbort.')