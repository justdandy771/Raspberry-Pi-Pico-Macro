import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS


keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)


"""

Each of these can be renamed to what you would like to use
Based on research I've done GPIO pin 15 acts up sometimes, feel free to use that pin if you find no issues

"""

button1 = board.GP1       
button2 = board.GP2
button3 = board.GP3
button4 = board.GP4
button5 = board.GP5
button6 = board.GP6
button7 = board.GP7
button8 = board.GP8
button9 = board.GP9
button10 = board.GP10
button11 = board.GP11
button12 = board.GP12
button13 = board.GP13
button14 = board.GP14
button15 = board.GP16
button16 = board.GP17
button17 = board.GP18
button18 = board.GP19
button19 = board.GP20
button20 = board.GP21
button21 = board.GP22

"""

Initializing Buttons

Since this is a keyboard emulating script the buttons are all inputs
Call in the button with digitalio.DigitalInOut() with each of the above buttons
Next determine the direction of the button, in this case its an input
Finally setting the intial state to UP or Down

"""
test_print = digitalio.DigitalInOut(test1)
test_print.direction = digitalio.Direction.INPUT
test_print.pull = digitalio.Pull.DOWN


macro = digitalio.DigitalInOut(test2)
macro.direction = digitalio.Direction.INPUT
macro.pull = digitalio.Pull.DOWN

test_print_bool = False
macro_bool = False

"""
For the main program you can choose between the following:
Printing out text with layout.write()
Sending Macro shortcuts using keyboard.press()

All keyboard mappings can be found at
"https://circuitpython.readthedocs.io/projects/hid/en/latest/_modules/adafruit_hid/keycode.html"

Check if button is pressed and execute the macro/print the specified text

Remember to use sleep after each of the key presses to ensure that there is a break in the input

After sending a macro function to the computer the keys need to also be released manually

"""


while True:
	 
    if test_print.value:  
        layout.write('test value printed here')
        time.sleep(0.15)
        test_print_bool = not test_print_bool

    if macro.value:
        keyboard.press(Keycode.CONTROL, Keycode.ALT, Keycode.DELETE)
        time.sleep(0.15)
        keyboard.release(Keycode.CONTROL, Keycode.ALT, Keycode.DELETE)
        macro_bool = not macro_bool

