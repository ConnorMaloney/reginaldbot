
# Woodcutting bot at Varrock, near Bank of Gielinor
# NOTE: Upon every left/right orientation, X-values seem to be changing by a factor of around ~10. This greatly affects the accuracy and produces undesired results.
#       Does this have to do with pyautogui.pause()? Time.sleep(1.3) and pyautogui.pause(1.3) seem to both have different times?
#       X-values appearing way off. I'd imagine this is runescape's doing. Or OSBuddy's.

#       UPDATE: Nevermind, looks like it has to do because I lose some orientation between the left pan and right pan. However, resetting to north after
#       each pan should keep me on track.

#       HUGE UPDATE: EVERY TIME I AM RESETTING ORIENTATION, IT CHANGES X-AXIS BY ~10 PIXELS (-10 then +10 pixels, repeat)
#       UPDATE 3: Nevermind... is it random? I keep testing orientation. I swear it has changed it. (Unless this is pyautogui.pause failing, or its a human error and I stop it abruptly)
#       No, there is DEFINITELY some variation with all of this. Thus, I'm going to have to always be looking north. I can't change the camera angle.


# Import modules
import pyautogui, time, sys

# Set 1.3 second delay after every pyautogui call
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
print("Orienting...\n")
pyautogui.click(1756, 54)
# pyautogui.scroll(-100) # Ensure that game is scrolled out as far as possible
pyautogui.keyDown('up')
pyautogui.keyUp('up')

try:
    while i < 3:
        pyautogui.click(258, 984) # Travels to second wooden post near oak tree (13s travel time)
        for i in range(13,0,-1):
            numStr = "Walking to oak tree... " + str(i).rjust(4)
            print(numStr, end='')
            print('\b' * len(numStr), end='', flush=True)
            time.sleep(1)
        print("\n")
        pyautogui.moveTo(956, 661) # Hover over chop
        pyautogui.click(956, 661) # Click chop
        for i in range(0,20,+1):
            pyautogui.click(956, 602) #Clicking on stump (doesnt move)
            numStr = "Chopping" + str(i).rjust(4) + " times..."
            print(numStr, end='')
            print('\b' * len(numStr), end='', flush=True)
            time.sleep(5)
        print("\n")

        pyautogui.moveTo(1408, 234) # Hover over bank booth button
        pyautogui.click(1408, 234) # Click bank booth

        for i in range(13,0,-1):
            numStr = "Walking to bank... " + str(i).rjust(4)
            print(numStr, end='')
            print('\b' * len(numStr), end='', flush=True)
            time.sleep(1)
        print("\n")

        print("Depositing...")
        pyautogui.click(1792,755) # First oak log
        time.sleep(0.2)
        pyautogui.click(1076,69) # Bank menu close button
        print("\n")
        i+=1



    
    # Having trouble implementing screencapture
    # pyautogui.moveTo(989,488) # Hover over oak button
    # time.sleep(3)
    # oakButtonLocation = pyautogui.locateOnScreen('ChopOakPic.PNG', region=(990, 505, 200, 200))
    # print(oakButtonLocation)

    
    #(1332,181) Clicking on Bank Bank Booth from stump
 #   for i in range(3,0,-1): 
        # Testing
  #      pyautogui.keyDown('right')
   #     pyautogui.keyUp('right')
    #    pyautogui.keyDown('left')
     #   pyautogui.keyUp('left')

except KeyboardInterrupt:
    print('\nAbort.')