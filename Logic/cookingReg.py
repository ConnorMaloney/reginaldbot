# Import modules
import pyautogui, time, sys

# Handle emergency termination
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

# Testing loop dragging functions for combining ingredients
print('Cooking bot. Press Ctrl-C to quit.')
print("Starting bot in...")
for i in range(5,0,-1):
    sys.stdout.write(str(i)+' ')
    sys.stdout.flush()
    time.sleep(1)

pyautogui.click() # Click brings in focus
distance = 200
try: 
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.2)   # move right
        distance = distance - 5
        pyautogui.dragRel(0, distance, duration=0.2)   # move down
        pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
        distance = distance - 5
        pyautogui.dragRel(0, -distance, duration=0.2)  # move up
except KeyboardInterrupt:
    print('\nAbort.')