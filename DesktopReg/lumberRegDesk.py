
# Woodcutting bot at Varrock, near Bank of Gielinor
# NOTE: Upon every left/right orientation, X-values seem to be changing by a factor of around ~10. This greatly affects the accuracy and produces undesired results.
#       Does this have to do with pyautogui.pause()? Time.sleep(1.3) and pyautogui.pause(1.3) seem to both have different times?
#       X-values appearing way off. I'd imagine this is runescape's doing. Or OSBuddy's.

#       UPDATE: Nevermind, looks like it has to do because I lose some orientation between the left pan and right pan. However, resetting to north after
#       each pan should keep me on track.

#       HUGE UPDATE: EVERY TIME I AM RESETTING ORIENTATION, IT CHANGES X-AXIS BY ~10 PIXELS (-10 then +10 pixels, repeat)
#       UPDATE 3: Nevermind... is it random? I keep testing orientation. I swear it has changed it. (Unless this is pyautogui.pause failing, or its a human error and I stop it abruptly)
#       No, there is DEFINITELY some variation with all of this. Thus, I'm going to have to always be looking north. I can't change the camera angle.


# New Location 2: Draynor village bank.
# Start position: Right in front of banker closest to door
# Travel position: (1325,597)
# Stump position: (1025, 535) continuously click here
# Banker position from stump: (610, 468)

# Import modules
import pyautogui, time, sys

# Set 0.5 second delay after every pyautogui call
pyautogui.PAUSE = 0.5
# Handle emergency termination (move mouse to upper left of screen)
# pyautogui.FAILSAFE = True
# Disabled as it's currently buggy

#
print('\nWelcome to OSRS Woodcutting bot. Reginald, at your service.\n')

print(r"""
       ___                                                                
      /___\                                                 
     (|0 0|)                                                    
   __/{\U/}\_ ___/vvv                                                
  / \  {~}   / _|_P|                                                 
  | /\  ~   /_/   ||                                                 
  |_| (____)      ||                       
  \_]/______\  /\_||_/\ 
     _\_||_/_ |] _||_ [|            
    (_,_||_,_) \/ [] \/
""")

print('Where am I chopping today?\n')
print('(1)  Varrock\n')
print('(2)  Draynor\n')
print('(0)  Nowhere\n')
choice = input('Please enter your choice: ')

# Handle Varrock
if choice ==  '1':
    print('WORKIN ON IT')
    """
    print('Cutting oak logs at Varrock. Press Ctrl-C to quit.')
    print("Starting reginald in...\n")
    for i in range(5,0,-1):
        print(i, end='')
        print('\b' * len(str(i)), end='', flush=True)
        time.sleep(1)

    # Orients camera north
    print("Orienting...\n")
    pyautogui.click(1756, 54)
    # pyautogui.scroll(-100) # Ensure that game is scrolled out as far as possible
    pyautogui.keyDown('up', pause=1.3)
    pyautogui.keyUp('up')

    try:
        while True:
            pyautogui.click(1760, 165) # Clicks sprint button (switch to sprinting)
            pyautogui.moveTo(258, 984) # Hovers to wooden post
            pyautogui.click(258, 984) # Travels to second wooden post near oak tree (13s travel time walking, 7s sprinting)
            for i in range(7,0,-1):
                numStr = "Running to oak tree... " + str(i).rjust(4)
                print(numStr, end='')
                print('\b' * len(numStr), end='', flush=True)
                time.sleep(1)
            print("\n")
            pyautogui.moveTo(956, 635) # Hover over chop
            pyautogui.click(956, 635) # Click chop
            for i in range(0,19,+1):
                pyautogui.click(956, 602) #Clicking on stump (doesnt move)
                numStr = "Chopping" + str(i).rjust(4) + " times..."
                print(numStr, end='')
                print('\b' * len(numStr), end='', flush=True)
                time.sleep(4.2)
            print("\n")

            pyautogui.click(1760, 165) # Clicks sprint button (switch to walking)
            pyautogui.moveTo(1422, 222) # Hover over bank booth button
            pyautogui.click(1422, 222) # Click bank booth

            for i in range(13,0,-1):
                numStr = "Walking to bank... " + str(i).rjust(4)
                print(numStr, end='')
                print('\b' * len(numStr), end='', flush=True)
                time.sleep(1)
            print("\n")

            print("Depositing...")
            pyautogui.click(1792,755) # First oak log
            time.sleep(2) # Account for any lag
            pyautogui.click(1076,69) # Bank menu close button
            time.sleep(2)
            print("\n")

    except KeyboardInterrupt:
        print('\nAbort.')
        """

# Handle Draynor
elif choice == '2':
    print('Draynor it is! Lets get to choppin. Press Ctrl-C to quit.')
    print("Starting reginald in...\n")
    for i in range(5,0,-1):
        print(i, end='')
        print('\b' * len(str(i)), end='', flush=True)
        time.sleep(1)

    # Orients camera north
    print("Orienting...\n")
    pyautogui.click(1757, 55) # Clicks compass
    # pyautogui.scroll(-100) # Ensure that game is scrolled out as far as possible
    pyautogui.keyDown('up', pause=1.3)
    pyautogui.keyUp('up')
    pyautogui.click(1759, 167) # Clicks sprint button


    try:
        while True:
            pyautogui.moveTo(1286, 608) # Moves to oak tree and hovers over
            pyautogui.click(1286, 608) # Travels to location/cuts oak

            for i in range(5,0,-1):
                numStr = "Running to oak tree... " + str(i).rjust(4)
                print(numStr, end='')
                print('\b' * len(numStr), end='', flush=True)
                time.sleep(1)
            print("\n")

            pyautogui.moveTo(1026 ,535) # Hovers over tree to chop first time
            for i in range(0,17,+1):
                pyautogui.click(1026, 535) #Clicking on stump (doesnt move)
                numStr = "Chopping" + str(i).rjust(4) + " times..."
                print(numStr, end='')
                print('\b' * len(numStr), end='', flush=True)
                time.sleep(4.2)
            print("\n")

            pyautogui.moveTo(611, 470) # Hover over bank booth button
            pyautogui.click(611, 470) # Click bank booth
            for i in range(5,0,-1):
                numStr = "Running to bank... " + str(i).rjust(4)
                print(numStr, end='')
                print('\b' * len(numStr), end='', flush=True)
                time.sleep(1)
            print("\n")

            print("Depositing...")
            pyautogui.click(1791, 758) # First oak log
            time.sleep(1.5) # Account for any lag
            pyautogui.click(1079, 69) # Bank menu close button
            time.sleep(1.5)
            print("\n")

    except KeyboardInterrupt:
        print('\nAbort.')

# Handle quit
else:
    print('Nowhere eh? Such a pity. Farewell then.')