import pyautogui

"""
FAIL-SAFE : Move your mouse to any corner of your screen to stop pyautogui from controlling your mouse or keyboard


(0,0) is the top-left of your screen

X increases as you move the mouse to the right
Y increases as you move the mouse lower
"""

width, height = pyautogui.size() # Size of your computer screen

print(pyautogui.position()) # Current position of your mouse on your screen

pyautogui.moveTo(0,0,3) # x,y,time (top-left) moves to the specified position in 3 seconds
pyautogui.moveRel(xOffset=500,yOffset=500,duration=5) # 500 pixels towards right and 500 pixels down in 5 seconds
pyautogui.click(116,11) # Click at (x,y)
pyautogui.doubleClick(700,500) # Double click at (x,y)
pyautogui.rightClick() # where ever the mouse is
pyautogui.displayMousePosition()
# Continuously displays the mouse position

pyautogui.dragRel(xOffset=100,yOffset=100, button='left')
# Drags the mouse 100 pixels to the right and 100 pixels down while holding the left button
# button can be equal to 'right', 'left' or 'middle'

pyautogui.click(1409,812) ;pyautogui.typewrite("Hello world!",0.1) # keys and the interval in between
pyautogui.click(1409,512) ;pyautogui.typewrite(['a','c','left','b'],1) # keys and the interval in between
pyautogui.press('f1')
pyautogui.hotkey('command','o') # two keys together

pyautogui.alert('This is an alert box.')

result = pyautogui.confirm('Shall I proceed?')
option = pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C']) # label
# Both return a string value(label)
password = pyautogui.password('Enter password (text will be hidden)')
# Also returns a string

im1 = pyautogui.screenshot() # Screenshot of the whole screen
im2 = pyautogui.screenshot(region=(0, 0, 300, 400))
# Region(Left(X), Top(y), Height, Width)
pyautogui.screenshot(r'/Users/KailashT/Desktop/test.png') # Wherever you want to save the image

pyautogui.locateOnScreen(im1)
# Returns a 'Box' (x,y,height,width)
pyautogui.locateCenterOnScreen(im2)
# Return a point(Center of the image)

ss = pyautogui.screenshot()
pixel = ss.getpixel(((953, 626))) # X and Y coordinates of the pixel
# getpixel returns a color value
pyautogui.pixelMatchesColor(953, 626, (13, 45, 58, 255))
pyautogui.pixelMatchesColor(953, 626, pixel)
# X and Y coordinates inside the first parenthesis and the color value inside another nested parenthesis
# Returns a boolean value

# The result we get is the same even if we remove the last integer of the color value(stored in 'pixel')

pyautogui.KEYBOARD_KEYSpyautogui.KEYBOARD_KEYS # Returns the following
# Names of different keyboard commands
#   '\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/'
#   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
#   ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`','{', '|', '}', '~'
#   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
#        'u', 'v', 'w', 'x', 'y', 'z'
#   'accept', 'add', 'alt', 'altleft', 'altright', 'apps'
#   'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop'
#   'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete','backspace'
#   'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute'
#   'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20'
#        'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9'
#   'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji'
#   'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left'
#   'modechange', 'multiply', 'nexttrack', 'nonconvert'
#   'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock'
#   'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack'
#   'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr'
#   'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright'
#   'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup'
#   'win', 'winleft','winright', 'yen', 'command', 'option', 'optionleft', 'optionright'
