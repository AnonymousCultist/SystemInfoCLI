# Making a tool i guess

import os
import win32gui
import pygetwindow as gw
from termcolor import colored, cprint
import platform 
import psutil 

def green_text(words):
    for i in words:
        cprint(i, "green")

# Just a cool ascii picture
green_text(["  __     ___  ___  ___  ", " |   \\  |    |    |   |", " |    | |=-  |=-  |---' ", " |___/  |___ |___ |     "])
text = colored("o---|-----------------------", "red", attrs=["blink"])
print(text)
green_text(["   /^^\\", " \\______/", "  [ 00 ]    /   ___  ___ _____  __   __  ", "   [==]    /__ |    |      |   |  | |__| ", "   /]['*     / |=-  |      |   |  | | \\ ", "   /  \\     /  |___ |___   |   |__| |  \\"])
redtext2 = colored("o---|------------------------------\n", "red", attrs=["blink"])
print("        ", redtext2)

newtext = colored("System: ", "red")
print(newtext, colored(platform.system(), "magenta")) 
newtext2 = colored("Node Name: ", "red")
print(newtext2, colored(platform.node(), "magenta")) 
newtext3 = colored("Release: ", "red")
print(newtext3, colored(platform.release(), "magenta")) 
newtext4 = colored("Version: ", "red")
print(newtext4, colored(platform.version(), "magenta")) 
newtext5 = colored("Machine: ", "red")
print(newtext5, colored(platform.machine(), "magenta")) 
newtext6 = colored("Processor: ", "red")
print(newtext6, colored(platform.processor(), "magenta")) 
newtext7 = colored("CPU Count: ", "red")
print(newtext7, colored(psutil.cpu_count(), "magenta"))
newtext8 = colored("Memory Info: ", "red")
print(newtext8, colored(psutil.virtual_memory(), "magenta"))

current_dir = os.getcwd()
newtext9 = colored("Current Dir: ", "red")
print(newtext9, colored(current_dir, "magenta"))


#####
def enum_window_callback(hwnd, windows): 
    # This callback function gets called for each top-level window 
    if win32gui.IsWindowVisible(hwnd): 
        # Check if the window is visible 
        window_text = win32gui.GetWindowText(hwnd) 
        # Get the window title 
        if window_text: 
            # Only add windows with a title 
            windows.append((hwnd, window_text)) 
# List to store window handles and titles 
windows = [] 
# Enumerate all top-level windows 
win32gui.EnumDesktopWindows(None, enum_window_callback, windows) 
newtext10 = colored("Currently Open Windows: ", "red")
print(newtext10)
# Print the window handles and titles 
for hwnd, title in windows: print(colored("    Window handle: ", "yellow"), colored(hwnd, "green"), colored(" Title: ", "yellow"), colored(title, "green"))
#####
