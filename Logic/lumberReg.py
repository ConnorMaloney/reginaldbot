# Import modules
import pyautogui, time, sys

# Woodcutting bot at Varrock

# Important coordinates
# COMPASS - Can differ by 8 pixels
# ~(797, 56) - Position of orientation button 
# 
# BANK - Can differ by 2 pixels
# ~(548, 525) - Position of varrock banker (closest to south door)
# ~(230, 100) - Position of bank tab 1 (where oak logs are)
# ~(245, 145) - Position of logs in bank inv
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
# ~(835, 750) - Position of 2nd item in inventoryUniverse-Wallpaper-1920x1080-PIC-WPXH28693
#
#
# GRAND EXCHANGE COORDS
# ~(400, 400) - Position of grand exchange clerk (on rightside from right corner)

# Important Notes: Takes ~53 seconds to smelt 23 gold necklaces. Crafting levelup can popup at anytime
# and interrupt this process. Press spacebar 3-5 times to skip over this.

# Other bots? Progpmaker and Hoontar00
# Handle emergency termination
pyautogui.PAUSE = 2
pyautogui.FAILSAFE = True